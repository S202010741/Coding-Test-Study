import sys

##1. 입력받기
A,B,C = map(int,sys.stdin.readline().split())
    
##2. 내장함수 pow() 사용하여 결과 출력하기
print(pow(A,B,C))