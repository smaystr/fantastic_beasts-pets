#!/usr/bin/env python
import sys

F = "f"
U = "u"
D = "d"
S = "s"
E = "e"

up = "up"
down = "down"
stop = "stop"


def parse_input(input_line):
    d = {U: [], D: [], E:[]}
    split_line = input_line.split()
    d[F] = int(split_line[0])
    for b in split_line[1:]:
        bt = b[0]
        f = int(b[1:])
        d[bt].append(f)
    return d


class Elevator:

    def __init__(self):
        self._state_input_handler = self._stopped

    def input(self, input_line):
        input_d = parse_input(input_line)
        return self._state_input_handler(input_d)

    def _stopped(self, input_d):
        self._state_input_handler = self._up
        return (up, up)

    def _up(self, input_d):
        self._state_input_handler = self._stopped
        return (stop, up)


if __name__=='__main__':
    e = Elevator()
    for line in sys.stdin:
        action, indication = e.input(line)
        print "%s ----> %s, %s" % (line.strip(), action, indication)
