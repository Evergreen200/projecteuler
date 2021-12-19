def solution(N: int = 1000) -> int:
    sum: int = 0
    for i in range(N):
        sum += i if i % 3 == 0 or i % 5 == 0 else 0
    return sum


if __name__ == "__main__":
    print(solution())
