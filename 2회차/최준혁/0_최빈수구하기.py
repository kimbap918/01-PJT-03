# [제약 사항]
# 학생의 수는 1000명, 각 학생의 점수는 0점 이상 100점 이하의 값
# 최빈수가 같으면 가장 큰 수를 출력할것 
# 최빈수 : 특정 자료에서 가장 여러 번 나타나는 값
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3 최빈수 = 8

# 첫 줄에 테스트 케이스가 주어진다.
T = int(input())
# T번의 케이스 동안
for i in range(1, T+1):
    # 공백을 사이에 두고 입력
    score = input().split() # 10, 10, 20, 10, 20
    # 같은값들을 어떻게 처리할까? set에 넣고 카운트?
    set_score = list(set(score)) #[10, 20]
    # print(set_score) 출력 확인
    cnt = [] # 카운트를 위한 리스트 생성
    for sc_cnt in set_score: # set_score의 값들 안에서 
        # score의 값들을 카운트하고 cnt에 넣는다
        cnt.append(score.count(sc_cnt)) # 10 10 20 10 20 [1, 4]

    print("#{} {}".format(i, set_score[cnt.index(max(cnt))]))

## 접근 방법이 잘못된것같아요ㅠ 최빈수가 같은 경우를 못구했다.. 

# 22.07.29 21:31 수정
# T = int(input()) # 테스트 케이스의 수

# for i in range(1, T+1):
#     n = int(input()) # 테스트케이스의 번호
#     most = {} # 번호의 값과 카운트를 담을 딕셔너리
#     number = map(int, input().split()) 

#     for j in number: 
#         if j not in most: # 입력값이 딕셔너리 안에 없으면 
#             most[j] = 1 # 카운트 1
#         else:
#             most[j] += 1 # 카운트 1 증가

#     result = sorted(most.keys(), reverse= True) # 딕셔너리의 키 값을 내림차순 정렬
#     print("#{} {}".format(n, max(result, key=most.get))) # 최대값 산출 후 출력