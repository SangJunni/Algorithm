import re
import functools


def parse_input(s):
    pattern = re.compile('[a-zA-Z]|\d+')
    return pattern.findall(s)


def compare_values(a, b):
    if a == b:
        return 0
    return 1 if a < b else -1


def custom_compare(a, b):
    if a.isdigit() != b.isdigit():
        return compare_values(b.isdigit(), a.isdigit())
    elif a.isdigit():
        return compare_values(int(a), int(b)) if int(a) != int(b) else compare_values(len(a) - len(a.lstrip('0')), len(b) - len(b.lstrip('0')))
    elif a.lower() != b.lower():
        return compare_values(a.lower(), b.lower())
    else:
        return compare_values(a, b)

@functools.cmp_to_key
def comparator(a, b):
    parsed_a = parse_input(a)
    parsed_b = parse_input(b)
    for i in range(min(len(parsed_a), len(parsed_b))):
        if parsed_a[i] != parsed_b[i]:
            return custom_compare(parsed_a[i], parsed_b[i])
    return compare_values(len(parsed_a), len(parsed_b))


n = int(input())
strings = [input() for _ in range(n)]
strings.sort(key=comparator, reverse=True)
print(*strings, sep='\n')
