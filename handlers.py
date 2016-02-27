__author__ = 'ziling'


class Handler(object):
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def stop(self, name):
        self.callback('stop_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                return match.group(0)

            return result
        return substitution


class HTMLRenderer(Handler):
    def start_document(self):
        print '<html><head><title>...</title></head><body>'

    def stop_document(self):
        print '</body></html>'

    def start_paragraph(self):
        print '<p>'

    def stop_paragraph(self):
        print '</p>'

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def feed(self, data):
        print data

