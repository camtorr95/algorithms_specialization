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
    x = 31
    m = 1000000007

    def __init__(self, k: int, s: str, t: str):
        """Initialize the solver with the number of mismatches (k), the first string (s), and the second string (t)."""
        self.k = k
        self.s = s
        self.t = t
        self.h_s = [hash_function(s[:i], self.x, self.m) for i in range(len(s) + 1)]
        self.h_t = [hash_function(t[:i], self.x, self.m) for i in range(len(t) + 1)]

    def hash_s(self, l: int, u: int):
        """Compute the hash value of the substring of s from index (l) to index (u).
        l stands for lower and u stands for upper bound.
        """
        return compute_hash(self.h_s, self.m, self.x, l, u - l + 1)

    def hash_t(self, l: int, u: int):
        """Compute the hash value of the substring of t from index (l) to index (u).
        l stands for lower and u stands for upper bound.
        """
        return compute_hash(self.h_t, self.m, self.x, l, u - l + 1)

    def search_mismatches(self, l_s: int, u_s: int, l_t: int, u_t: int, errors: int = 0):
        """Search for mismatches in the two strings using binary search. Return the number of mismatches found up to one above the maximum
        number of errors (k).

        If we needed the total number of mismatches instead, the errors validation with the k value should be removed or commented out.

        Args:
            l_s (int): lower bound of the substring of s
            u_s (int): upper bound of the substring of s
            l_t (int): lower bound of the substring of t
            u_t (int): upper bound of the substring of t
            errors (int, optional): number of errors found so far. Defaults to 0, however is a crucial parameter for the recursive calls to
                account for the number of errors found so far.
        Returns:
            int: number of mismatches found up to one above the maximum number of errors (k).
        """
        # stop if there are no more characters to compare
        if l_s > u_s or l_t > u_t:
            return 0

        # find the middle index
        i_s = (l_s + u_s) // 2
        i_t = (l_t + u_t) // 2

        # check if the middle characters are equal
        if self.s[i_s] != self.t[i_t]:
            errors += 1

        # stop if the number of errors is greater than k
        if errors > self.k:
            return errors

        # Calculate the hash values of the left and right halves of the strings without the middle character.
        hs_l, hs_r = self.hash_s(l_s, i_s - 1), self.hash_s(i_s + 1, u_s)  # hash of the left and right halves of s
        ht_l, ht_r = self.hash_t(l_t, i_t - 1), self.hash_t(i_t + 1, u_t)  # hash of the left and right halves of t

        # search for mismatches in the left and right halves of the strings if the hash values are different
        left_errors, right_errors = 0, 0
        # pass the number of errors found so far to the recursive calls to avoid searching beyond the maximum number of errors
        # then subtract them in order to get the accurate count for each half
        if hs_l != ht_l:
            left_errors = self.search_mismatches(l_s, i_s - 1, l_t, i_t - 1, errors) - errors
        if hs_r != ht_r:
            right_errors = self.search_mismatches(i_s + 1, u_s, i_t + 1, u_t, errors) - errors

        return errors + left_errors + right_errors

    def solve(self):
        ans = []
        for i in range(len(self.s) - len(self.t) + 1):
            if self.search_mismatches(i, i + len(self.t) - 1, 0, len(self.t) - 1) <= self.k:
                ans.append(i)
        return ans


def main():
    for line in sys.stdin.readlines():
        k, t, p = line.split()
        ans = Solver(int(k), t, p).solve()
        print(len(ans), *ans)


if __name__ == '__main__':
    main()
