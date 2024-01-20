# python3

import sys

cache_x1 = [0] * 500_001


def hash_function(s: str, x: int, p: int, cache: list) -> int:
    """Inverted polynomial hash function for precomputing the hash values of all substrings of s."""
    hash_value = 0
    for i in range(len(s)):
        exp = len(s) - i - 1
        if cache[exp] == 0:
            cache[exp] = pow(x, exp, p)
        y = cache[exp]
        hash_value = (hash_value + ord(s[i]) * y) % p
    return hash_value


def compute_hash(h: list, m: int, x: int, a: int, l: int, cache: list) -> int:
    """Compute the hash value of a substring of length (l) starting at index (a) using the precomputed hash values."""
    if cache[l] == 0:
        cache[l] = pow(x, l, m)
    y = cache[l]
    return (h[a + l] - h[a] * y) % m


class Solver:
    x_1 = 1117
    x_2 = 3331
    m_1 = 1000000007
    m_2 = 1000000009

    def __init__(self, s):
        self.cache_x1 = {}
        # self.cache_x2 = {}
        self.h_1 = [hash_function(s[:i], self.x_1, self.m_1, cache_x1) for i in range(len(s) + 1)]
        # self.h_2 = [hash_function(s[:i], self.x_2, self.m_2) for i in range(len(s) + 1)]
        self.s = s

    def compute_hash_1(self, a, l) -> int:
        return compute_hash(self.h_1, self.m_1, self.x_1, a, l, cache_x1)

    def ask(self, a, b, l) -> bool:
        # compute_hash(self.h_2, self.m_2, self.x_2, a, l) == compute_hash(self.h_2, self.m_2, self.x_2, b, l))
        return self.compute_hash_1(a, l) == self.compute_hash_1(b, l)


def main():
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")


if __name__ == '__main__':
    main()
