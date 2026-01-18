def main():
    r, b = map(int, input().split())
    t = 2 - r // 2
    d = t**2 - 4 * b
    w = (-t + int(d**0.5)) // 2
    h = (-t - int(d**0.5)) // 2
    print(w + 2, h + 2)


if __name__ == "__main__":
    main()
