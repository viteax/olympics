PRIMES = ["2", "3", "5", "7"]


def count_primes_lower_than(s: str, do_count=False):
    res = 0
    for i in range(len(s)):
        if s[i] != "1":
            if s[i] == "0":
                return 0
            break
    for i in range(len(s)):
        if s[i] != "1":
            res += sum(prime < s[i] for prime in PRIMES)
            if s[i] in PRIMES:
                for j in range(i + 1, len(s)):
                    if s[j] != "1":
                        if s[j] == "0":
                            break
                        res += 1
                        break
                if (i + 1 == len(s) or s[j] == "1") and do_count:
                    res += 1
            res += 4 * (len(s) - i - 1)
            break
    return res


def solve(l, r):
    l, r = str(l), str(r)
    ans = 2 * (len(r) - 1) * len(r)
    ans += count_primes_lower_than(r, do_count=True)
    ans -= 2 * (len(l) - 1) * len(l)
    ans -= count_primes_lower_than(l)
    return ans


l = input().strip()
r = input().strip()
print(solve(l, r))
