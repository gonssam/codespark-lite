# 변수 선언, 변수 연산(덧셈)
a=1
b=2
c=a+b
print(a+b)

# 곱셈
print(a*b)

# input:입력
a= int(input("first number: "))
b= int(input("second number: "))

# 처리
c=a+b

# 출력
print(a+b)

# input:입력
a= int(input("first number: "))
b= int(input("second number: "))

# 처리
def adder(a,b):
    return a+b

# 출력
print(adder(a,b))

print("========================================")
# 자동화
while True:
    a= int(input("first number (999 for quit): "))
    if a == 999:
        print("bye~~")
        break
    else:
        b= int(input("second number: "))
    print(adder(a,b))