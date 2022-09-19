# 짝수와 홀

# def solution(num):
#     if num%2==0:
#         return 'Even'
#     else:
#         return 'Odd'

# print(solution(2))
# print(solution(3))


# 자릿수 더하기

# def solution(n):
#     return sum(map(int, list(str(n))))

# print(solution(32))
# print(solution(153))


# 약수의 합

# Ver.1
# def solution(n):    
#     return n + sum([i for i in range(1, int(n//2)+1) if n % i == 0])

# print(solution(12))

# Ver.2
# def solution(n):
#     result = 0

#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             result += i + (n//i)    # 짝으로 더하기
#     return result

# print(solution(12))


# 평균 구하기

# def solution(arr):
#     return (sum(arr) / len(arr))


# 정수 제곱근 판별

def solution(n):
    sqrt = n**(1/2)
    
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    else: return -1

print(solution(121))
print(solution(11))