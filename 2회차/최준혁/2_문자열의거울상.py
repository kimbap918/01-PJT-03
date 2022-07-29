# bdppq = pqqbd
# b = d, d = b, p = q, q = p

# 테스트케이스
T = int(input())

for t in range(1, T+1): # 1부터 T+1까지
    S = input() # 문자열을 입력받음

    answer = '' # 거울상을 누적시킬 변수
    for i in range(len(S) - 1, -1, -1): # 문자열의 역순으로 진행
        if S[i] == 'b': 
            answer += 'd'
        elif S[i] == 'd':
            answer += 'b'
        elif S[i] == 'p':
            answer += 'q'
        else:
            answer += 'p'
        # 각각의 문자를 거울상으로 변경 후에 answer에 누적
    print("#{} {}".format(t, answer))