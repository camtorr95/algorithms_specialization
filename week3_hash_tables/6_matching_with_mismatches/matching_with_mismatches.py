# python3

import sys


def solve(k, text, pattern):
    return []


def main():
    for line in sys.stdin.readlines():
        k, t, p = line.split()
        ans = solve(int(k), t, p)
        print(len(ans), *ans)


if __name__ == '__main__':
    main()
