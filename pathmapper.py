import re

class PathMapper(object):
    def __init__(self, paths):
        self.paths = [(re.compile(regex),f) for regex,f in paths]

    def map(self, path):
        for regex,f in self.paths:
            match = regex.match(path)
            if match:
                return match,f
        return None, None

    def resolve(self, path):
        match, f = self.map(path)
        if match:
            # If we have dictionary arguments, we have to ignore them from the groups field
            # otherwise for f(a,b=1) we get groups(a,b) and groupdict(b)
            if len(match.groupdict()):
                return f(*match.groups()[:-len(match.groupdict())], **match.groupdict())
            else:
                return f(*match.groups())
        return None, None
