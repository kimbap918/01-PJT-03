# 전체 테스트 케이스의 수
T = int(input())


for i in range(1, T+1):
    N = int(input()) # 테스트 케이스 
    p = list(map(int, input().split())) # 입력값을 정수로 받아 리스트에 담음
    ave = 0 # 평균을 구하기 위한 변수
    cnt = 0 # 카운트를 세기위한 변수

    # p리스트의 길이동안
    for j in range(len(p)):
        ave += p[j] # ave에 합산

    for k in p: # 리스트 p 내의 값 k가
        if k <= ave/len(p): # ave의 평균보다 값이 작거나 같다면
            cnt += 1 # 카운트 증가
    print("#{} {}".format(i, cnt))

