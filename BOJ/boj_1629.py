import sys

## 1. 입력받기
def solve() :
    line = sys.stdin.readline().split()
    if not line:
        return
    
    A, B, C = map(int, line)

    ## 2. 거듭제곱 계산하는 함수
    def power(a, b, c):
        # 지수가 1일 시 그냥 a를 c로 나눈 나머지 반환
        if b == 1:
            return a%C
        
        # 지수를 나누어 계산(분할정복)
        temp = power(a, b//2, c)

        # 지수가 짝수일 때
        if b % 2 == 0 :
            return (temp * temp)%c
        
        # 지수가 홀수일 때
        else :
            return (temp * temp * a)%C
        
    ## 3. 결과 반환
    print(power(A,B,C))
solve()
