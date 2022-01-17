def solution(n) -> int:
    x, y = 0, 1
    z = x + y
    sum = 0
    while x < n:
        if x % 2 == 0:
            sum += x
        x = y
        y = z
        z = x + y
    return sum

if __name__ == '__main__':
    print(solution(4000000))
