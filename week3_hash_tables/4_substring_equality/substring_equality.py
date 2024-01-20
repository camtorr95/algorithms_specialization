# python3

import sys


def hash_function(s: str, x: int, p: int):
    """Inverted polynomial hash function for precomputing the hash values of all substrings of s."""
    hash_value = 0
    for i in range(len(s)):
        exp = len(s) - i - 1
        y = pow(x, exp, p)
        hash_value = (hash_value + ord(s[i]) * y) % p
    return hash_value


def compute_hash(h: list, m: int, x: int, a: int, l: int):
    """Compute the hash value of a substring of length (l) starting at index (a) using the precomputed hash values."""
    y = pow(x, l, m)
    return (h[a + l] - h[a] * y) % m


class Solver:
    x_1 = 31
    x_2 = 11111
    m_1 = 1000000007
    m_2 = 1000000009

    def __init__(self, s):
        self.h_1 = [hash_function(s[:i], self.x_1, self.m_1) for i in range(len(s) + 1)]
        # self.h_2 = [hash_function(s[:i], self.x_2, self.m_2) for i in range(len(s) + 1)]
        self.s = s

    def ask(self, a, b, l):
        # compute_hash(self.h_2, self.m_2, self.x_2, a, l) == compute_hash(self.h_2, self.m_2, self.x_2, b, l))
        return compute_hash(self.h_1, self.m_1, self.x_1, a, l) == compute_hash(self.h_1, self.m_1, self.x_1, b, l)  # and


def main():
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")


if __name__ == '__main__':
    main()
