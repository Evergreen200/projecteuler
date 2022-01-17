def solution(N: int) -> int:
    sum = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    print(solution(1000))
