import random


_BRACKET_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def random(*, low=0, high=1):
    assert high >= low
    n = high - low
    r = random.random() * n
    return low + r


def choice(lst):
    return random.choice(lst)


def traverse_bracket(string, start_bracket="("):
    if string[0] != start_bracket:
        raise ValueError("no brackets found")

    end_bracket = _BRACKET_PAIRS[start_bracket]
    nesting_level = 1

    inside = ""
    rest = string[1:]
    while nesting_level != 1:
        if not rest:
            raise ValueError("brackets not properly balanced")
        char = rest[0]
        if char == start_bracket:
            nesting_level += 1
        elif char == end_bracket:
            nesting_level -= 1
            return (inside, rest)

        rest = rest[1:]
        inside += char