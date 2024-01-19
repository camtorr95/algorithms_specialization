# python3

import sys
from collections import namedtuple
from typing import Optional

Answer = namedtuple('answer_type', 'i j len')


def hash_function(s: str, x: int, p: int):
    hash_value = 0
    for i, c in enumerate(s):
        y = pow(x, i, p)
        hash_value = (hash_value + ord(c) * y) % p
    return hash_value


def precompute_hashes(text: str, p: int, x: int, l: int):
    """Precompute hashes for all substrings of text of length (l) for longest common substring matching."""
    last_index = len(text) - l
    hashes = [0] * (last_index + 1)  # zero as a placeholder for all hashes before precomputing
    hashes[last_index] = hash_function(text[-l:], x, p)
    y = pow(x, l, p)
    for i in range(len(text) - l - 1, - 1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + l])) % p
    return hashes


class Solver:
    x_1 = 31
    x_2 = 11111
    m_1 = 1000000007
    m_2 = 1000000009

    def __init__(self, s: str, t: str):
        """Precompute the hash values of all substrings of s and t.
        Args:
            s (str): First string.
            t (str): Second string.
        """
        # NO NEED TO PRECOMPUTE THE HASH VALUES OF ALL SUBSTRINGS OF S AND T.
        self.s = s
        self.t = t
        # Hash table to save all hash values of length k.
        self.hs_1: Optional[list] = None
        self.hs_2: Optional[list] = None
        self.ht_1: Optional[list] = None
        self.ht_2: Optional[list] = None

    def setup_precomputed_hashes(self, s, t, k):
        """Precompute the hash values of all substrings of s and t of length k."""
        self.hs_1 = precompute_hashes(s, self.m_1, self.x_1, k)
        self.hs_2 = precompute_hashes(s, self.m_2, self.x_2, k)
        self.ht_1 = precompute_hashes(t, self.m_1, self.x_1, k)
        self.ht_2 = precompute_hashes(t, self.m_2, self.x_2, k)

    def check(self, a, b):
        """Check if the substrings of s and t starting at a and b, respectively, have length l."""
        return self.hs_1[a] == self.ht_1[b] and self.hs_2[a] == self.ht_2[b]

    def find_substring(self, k) -> Optional[Answer]:
        """Find a substring of s and t of length k."""
        for i in range(len(self.s) - k + 1):
            for j in range(len(self.t) - k + 1):
                if self.check(i, j):
                    return Answer(i, j, k)
        return None

    def solve(self) -> Answer:
        """Find the longest common substring of s and t. Define k as the length of the longest common substring,
        starting as the length of the shortest string and decreasing until k = 0. Use binary search to find k.

        Returns:
            Answer: The answer to the problem.
        """
        # Define k as the length of the longest common substring, starting as the length of the shortest string and decreasing until k = 0.
        lower_bound = 0
        upper_bound = min(len(self.s), len(self.t))
        # Use binary search to find k.
        longest = Answer(0, 0, 0)
        while lower_bound <= upper_bound:
            k = (lower_bound + upper_bound) // 2
            self.setup_precomputed_hashes(self.s, self.t, k)
            current = self.find_substring(k)
            if current is not None:
                lower_bound = k + 1
                longest = current
            else:
                upper_bound = k - 1
        return longest


def main():
    for line in sys.stdin.readlines():
        s, t = line.split()
        solver = Solver(s, t)
        ans = solver.solve()
        print(ans.i, ans.j, ans.len)


if __name__ == "__main__":
    main()
