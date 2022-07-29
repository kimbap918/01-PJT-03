# 02.27 22:48 수정 
T = int(input()) 

for i in range(1, T+1):
    card = input() # card 값을 입력
    a = card.replace("-", "") # -를 제거하고 a에 담는다

    for j in range(len(a)):
        # a의 첫번째에 3, 4, 5, 6, 9가 있으면 
        if a[0] in ["3", "4", "5", "6", "9"]:
            check1 = 1 # check1 = 1
        else:
            check1 = 0 # 없다면 0
        if len(a) == 16: # 카드의 길이가 16이면 
            check2 = 1 # check2 = 1
        else:
            check2 = 0 # 아니면 0
    if check1 == 1 and check2 == 1: # check1 과 check2가 둘 다 1이면
        result = 1 # 결과는 1
    else:
        result = 0 # 아니면 0
    print("#{} {}".format(i, result))

