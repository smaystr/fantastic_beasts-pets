#!/usr/bin/env python
import sys

F = "f"
U = "u"
D = "d"
# S = "s"
E = "e"

up = "up"
down = "down"
stop = "stop"


def parse_input(input_line):
    d = {U: [], D: [], E: []}
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

    @staticmethod
    def _transition(input_d):
        floors_received = [item for sublist in input_d.values() if type(sublist) is list for item in sublist]
        max_floor_received = max(floors_received, default=0)
        transition = stop

        if input_d[F] and max_floor_received and (input_d[F] < max_floor_received):
            transition = up
        elif input_d[F] and max_floor_received and (input_d[F] >= max_floor_received):
            transition = down
            if (len(floors_received) == 1) and (input_d[F] == max_floor_received):
                transition = stop

        return transition

    def _stopped(self, input_d):
        transition = self._transition(input_d)
        state = stop

        if transition == up:
            self._state_input_handler = self._up
            if not ((input_d[F] in input_d[E]) and (input_d[F] in input_d[U])):
                state = up
        elif transition == down:
            self._state_input_handler = self._up
            if not ((input_d[F] in input_d[E]) and (input_d[F] in input_d[D])):
                state = down

        return state, transition

    def _up(self, input_d):
        transition = self._transition(input_d)
        state = up

        if transition == down:
            state = down

        if (input_d[F] in input_d[E]) or (input_d[F] in input_d[D]) or (input_d[F] in input_d[U]):
            self._state_input_handler = self._stopped
            state = stop

        return state, transition


if __name__ == '__main__':
    e = Elevator()
    for line in sys.stdin:
        action, indication = e.input(line)
        print("%s ----> %s, %s" % (line.strip(), action, indication))
