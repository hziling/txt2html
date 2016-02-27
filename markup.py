__author__ = 'ziling'
import re
import sys

from utils import blocks
from rules import ParagraphRule
from handlers import HTMLRenderer


class Parser(object):
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parser(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break

        self.handler.stop('document')


class BasicTextParser(Parser):
    def __init__(self, handler):
        super(BasicTextParser, self).__init__(handler)
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.+?)\*', 'emphasis')


handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parser(sys.stdin)
