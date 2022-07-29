# 제한 시간 내 풀지 못한 문제, 07.30 00:50 수정
# I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
# s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
for i in range(10):
    st = int(input()) # 원본 암호문 길이
    nd = list(map(int, input().split())) # 원본 암호문 
    rd = int(input()) # 명령어의 개수
    th = list(input().split()) # 삽입할 암호문의 값

    for j in range(len(th)): # 삽입할 암호문 리스트의 길이만큼
        if th[j] == "I": # I가 발견되면
            index = int(th[j+1]) # index에 x의 위치 1, 8, 3, 13, 3, 8, 4
            number = int(th[j+2]) # number에 y개의 숫자 5, 6, 8, 4, 4, 2, 10
            for h in range(number): # number의 y개 숫자 순회 01234, 012345, 01234567...
                # 원본 암호문의 x의 위치에서(index) 차례대로(+h) 
                # 삽입할 암호문(th)의 값을 넣어준다.(th[j+2+(h+1)]) 
                # j = 0 h = 0, th[3] = 400905 j = 0 h = 1, th[4] = 139831..
                # j = 8 h = 0, th[8] = 436704 j = 8 h = 1, th[9] = 702451..
                nd.insert(index+h,int(th[j+2+(h+1)])) 
                # print("index+h :"+str(index+h))
                # print("j+2+(h+1)"+str(j+2+(h+1)))
        else:
            continue
        # 테스트 케이스 번호 출력과 join으로 한 칸씩 띄워주면서 int 리스트인 nd를 형변환 한 후 10개 잘라 출력
    print("#{} {}".format(i+1, ' '.join(map(str, nd[0:10]))))
