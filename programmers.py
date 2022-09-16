# 짝수와 홀

# def solution(num):
#     if num%2==0:
#         return 'Even'
#     else:
#         return 'Odd'

# print(solution(2))
# print(solution(3))


# 자릿수 더하기

def solution(n):
    return sum(map(int, list(str(n))))

print(solution(32))
print(solution(153))
