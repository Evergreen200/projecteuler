def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0 and n != i:
            return False
    return True

def solution(n):
    for i in range(1, n):
        if n % i == 0:
            p = n // i
            if is_prime(p):
                return p


if __name__ == '__main__':
    print(solution(600851475143))
