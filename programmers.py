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

# def solution(s):
#     return int(s)

# print(solution('-1234'))

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
# def solution(x, n):
#     a = []
#     for i in range(1,n+1): # 콜론!!
#         a.append(i*x)
#     return a

    # for i in range(n):
    #     a.append((i+1)*x)
    # return a

# Ver.2 (choice)
# def number_generator(x, n):
#     return [(i+1) * x for i in range(n)]



# 나머지가 1이 되는 수 찾기

# Ver.1 (choice)
# def solution(n):
#     for i in range(1,n):
#         if n%i==1:
#             return i

# print(solution(12))

# Ver.2
# def solution(n):
#     return [x for x in range(1,n) if n%x==1][0]

    #     return min([x for x in range(1, n) if n % x == 1])


# 콜라츠 추측

# Ver.1 (choice)
# def solution(n):
#     c=0
#     while(n!=1):
#         if (n%2==0):
#             n/=2
#         else:
#             n=n*3+1
#         c+=1
#         if c>500:
#             c=-1
#             break
#     return c

# Ver.2
# def collatz(num):
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num*3 + 1
#         if num == 1:
#             return i + 1
#     return -1


# 두 정수 사이의 합

# Ver.1
# def solution(a, b):
#     if a==b:
#         return a
#     elif a<b:
#         return sum(i for i in range(a,b+1))
#     else:
#         return sum(i for i in range(b,a+1))

# Ver.2 (choice)
# def adder(a, b):
#     return sum(range(min(a,b),max(a,b)+1))


# 서울에서 김서방 찾기

# Ver.1 (choice)
# def findKim(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))

# Ver.2
# def solution(seoul):
#     return ('김서방은 %d에 있다' %seoul.index('Kim'))


# 핸드폰 번호 가리기 (문자열길이, 문자열 뒤에서 자르기)

# def hide_numbers(s):
#     return "*"*(len(s)-4) + s[-4:]


# 나누어 떨어지는 숫자 배열

# Ver.1 (choice)
# def solution(arr, divisor):
#     arr = [x for x in arr if x % divisor == 0]
#     arr.sort()
#     return arr if len(arr) != 0 else [-1]

# Ver.2
# def solution(arr, divisor): 
#     return sorted([n for n in arr if n%divisor == 0]) or [-1]


# 제일 작은 수 제거하기

# def solution(arr):
#     arr.remove(min(arr))
#     return arr if len(arr)!=0 else [-1]


# 음양 더하기

# Ver.1 
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# Ver.2 (choice)
# def solution(absolutes, signs):
#     s=0
#     for i in range(len(absolutes)):
#         if signs[i]:
#             s += absolutes[i]
#         else :
#             s -= absolutes[i]
#     return s


# 없는 숫자 더하기

# Ver.1 (choice)
# def solution(numbers):
#     a=0
#     for i in range(10):
#        if i not in numbers:
#             a+=i
#     return a


# Ver.2
# def solution(numbers):
#     return 45 - sum(numbers)


# 수박수박수박수박수박수?

# Ver.1 (choice)
# def solution(n):
#     s=""
#     for i in range(n):
#         if (i%2==0):
#             s+="수"
#         elif (i%2==1):
#             s+="박"
#     return s

# Ver.2
# def water_melon(n):
#     s = "수박" * n
#     return s[:n]

# Ver.3
# def water_melon(n):
#     return "수박"*(n//2) + "수"*(n%2)


# 가운데 글자 가져오기

# Ver.1
# def string_middle(str):
#     return str[(len(str)-1)//2:len(str)//2+1] # 맨끝 포함x


# Ver.2 (choice)
# def string_middle(str):
#     l = len(str)
#     if l%2==0:
#         return str[l//2-1:l//2+1]
#     else:
#         return str[l//2]


# 내적

# Ver.1 (choice)
# def solution(a, b):
#     return sum([x*y for x, y in zip(a,b)])

# Ver.2
# solution = lambda x, y: sum(a*b for a, b in zip(x, y))

# Ver.3
# def solution(a, b):
#     s=0
#     for i in range(len(a)):
#         s+=a[i]*b[i] 
#     return s

