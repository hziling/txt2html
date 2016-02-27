__author__ = 'ziling'


def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    import sys
    for block in blocks(sys.stdin):
        print block