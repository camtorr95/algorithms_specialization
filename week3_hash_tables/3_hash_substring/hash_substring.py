# python3
x = 1
p = 250000000007


def get_hash(s: str):
    hash_value = 0
    for i, c in enumerate(s):
        hash_value = (hash_value + ord(c) * x ** i) % p
    return hash_value


def precompute_hashes(text: str, l: int):
    """Precompute hashes for all substrings of text of length |pattern| (l) for the Rabin-Karp algorithm."""
    last_index = len(text) - l
    hashes = [0] * (last_index + 1)  # zero as a placeholder for all hashes before precomputing
    hashes[last_index] = get_hash(text[-l:])
    y = 1
    for i in range(1, l + 1):
        y = (y * x) % p
    for i in range(len(text) - l - 1, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + l])) % p
    return hashes


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    """Get occurrences of pattern in text using an optimized Rabin-Karp algorithm."""
    hashes = precompute_hashes(text, len(pattern))
    pattern_hash = get_hash(pattern)
    result = []

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash != hashes[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)

    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
