def is_palindrome(n: int) -> bool:
    s = str(n)
    h = int(len(s) / 2)
    s1 = s[:h]
    s2 = s[h:][::-1]
    is_palindrome = True
    for i in range(h):
        if s1[i] != s2[i]:
            is_palindrome = False
    return is_palindrome


def solution() -> int:
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            if is_palindrome(n) and n > largest_palindrome:
                largest_palindrome = n
    return largest_palindrome

if __name__ == "__main__":
    print(solution())
