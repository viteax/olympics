def is_equal(from1, from2, length, h, x, p):
    return (h[from1 + length - 1] + h[from2 - 1] * x[length]) % p == (
        h[from2 + length - 1] + h[from1 - 1] * x[length]
    ) % p


def count_hash_and_x(s: str):
    p = 10**9 + 7
    x_ = 257  # can be turned into 10 for debug
    s = "_" + s
    h = [0] * len(s)
    x = [1] * len(s)
    for i in range(1, len(s)):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        x[i] = x[i - 1] * x_ % p
    return h, x


s = "1213121"
h, x = count_hash_and_x(s)
print(is_equal(5, 1, 3, h, x, p=10**9 + 7))
