import sys

##1. 입력받기
A,B,C = map(int,sys.stdin.readline().split())
    
##2. 거듭제곱 계산
def power(a, b):
    # 지수가 1일 때
    if b == 1:
        return a%c
    # 지수 나누어 계산(분할정복)
    temp = power(a, b//2, c)

    # 지수가 짝수일 때
    if b%2 ==0 :
        return(temp*temp)%c
    #지수가 홀수일 때
    else:
        return (temp*temp*a)%c
    
    ##3. 결과반환
    print(power(A,B))