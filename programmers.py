# 짝수와 홀수

# Ver.1
# def solution(num):
#     if (num%2==0):
#         return "Even"
#     else:
#         return "Odd"

# print(solution(2))
# print(solution(3))

# Ver.2 (choice)
# def evenOrOdd(num):
#     return "Odd" if (num%2) else "Even"  #  0 >> false



# 자릿수 더하기

# Ver.1
# def solution(number):
#     a=0
#     while number%10>0:
#         a+=number%10
#         number=int(number/10)
#     return a

# print(solution(32))
# print(solution(153))    

# Ver.2
# def sum_digit(number):
#     return  number if number < 10 else number % 10 + sum_digit(number // 10) 

# Ver.3 (choice)
# def sum_digit(n):
#     return sum(map(int, list(str(n))))  # list(map(함수, 리스트)) : 리스트의 요소를 지정된 함수로 처리



# 약수의 합

# Ver.1
# def solution(num):
#     return sum([i for i in range(1,num+1) if num%i==0])

# print(solution(12))

# Ver.2
# def sumDivisor(n):    
#     return n + sum([i for i in range(1, int(n//2)+1) if n % i == 0])

# Ver.3
# def sumDivisor(n):
#     result = 0

#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             result += i + (n//i)    # 짝으로 더하기
#     return result



# 평균 구하기

# def solution(arr):
#     return (sum(arr) / len(arr))



# 정수 제곱근 판별

# Ver.1 (choice)
# def solution(n):
#     sqrt = n**(1/2)
#     return (sqrt+1)**2 if sqrt % 1 == 0 else -1

# print(solution(121))
# print(solution(11))

# Ver.2
# import math
# def nextSqure(n):
#     return 'no' if not math.sqrt(n).is_integer() else (math.sqrt(n)+1)**2



# 자연수 뒤집어 배열로 만들기

# Ver.1 (choice)
# def solution(n):
#     a=[]

#     while n>1:
#         a.append(int(n%10))
#         n/=10

#     return a

# print(solution(1234))

# Ver.2
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

# Ver.3 
# def digit_reverse(n):
#     arr =[]
#     for i in str(n):
#         arr.append(int(i))
#     arr.reverse() 
#     return arr



# 문자열 내 p와 y의 개수

# Ver.1 (choice)
# def solution(s):
#     return s.lower().count('p')==s.lower().count('y')

# print( solution("pPoooyY") )
# print( solution("Pyy") )

# Ver.2
# def numPY(s):
#     r = s.lower()
#     p,y=0,0
#     for char in r:
#         if char == 'p':
#             p+=1
#         elif char == 'y':
#             y+=1
#     if p==y:
#         return True
#     return False



# 하샤드 수

# Ver.1 (choice)
# def solution(x):
#     return x%sum(map(int, list(str(x))))==0

# print(solution(18))
# print(solution(13))

# Ver.2
# def Harshad(n):
#     return n % sum([int(c) for c in str(n)]) == 0



# 정수 내림차순으로 배치하기

# Ver.1 
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))

# Ver.2 (choice)
# def int_sort(n):
#     num=list(str(n))
#     num.sort(reverse=True)
#     answer=" "
#     for k in num:
#         answer+=str(k)
#     return int(answer)



# 문자열을 정수로 바꾸기

# Ver.1 (choice)

def solution(s):
    return int(s)

print(solution('-1234'))

# Ver.2
# def strToInt(str):
#     result = 0

#     for idx, number in enumerate(str[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             result += int(number) * (10 ** idx)

#     return result



# x만큼 간격이 있는 n개의 숫자

# Ver.1
def solution(x, n):
    a = []
    for i in range(1,n+1): # 콜론!!
        a.append(i*x)
    return a

    # for i in range(n):
    #     a.append((i+1)*x)
    # return a

# Ver.2
# def number_generator(x, n):
#     return [(i+1) * x for i in range(n)]
