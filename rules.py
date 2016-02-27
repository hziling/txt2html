__author__ = 'ziling'


class Rule(object):
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.stop(self.type)

        return True


class ParagraphRule(Rule):
    type = 'paragraph'

    def condition(self, block):
        return True
