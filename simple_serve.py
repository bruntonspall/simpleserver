import BaseHTTPServer
import pathmapper

def front(path):
    return [200, 'OK']

def rss(path):
    return [302, 'Redirect']

pm = pathmapper.PathMapper([
                           ('^/r2frontend/pages/Guardian(.*)/rss$', rss),
                           ('^/r2frontend/pages/Guardian(.*)$', front),
                           ])


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        (code, s) = pm.resolve(self.path)
        if code:
            self.send_response(code, self.responses[code])
            if code == 200:
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write('<h1>Test</h1>')
            else:
                self.send_header('Location', 'http://www.guardian.co.uk')
        else:
            self.send_response(404, 'Not Found')
            self.end_headers()
            self.wfile.write('Test')
    def do_HEAD(self):
        self.send_response(200)

server = BaseHTTPServer.HTTPServer(('', 8080), MyHandler)
server.serve_forever()
