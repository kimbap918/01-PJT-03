# 1) 매 홀수자리의 숫자마다 2를 곱해서 더합니다. 
# 2) 매 짝수자리의 숫자는 그대로 더합니다.
# 3) 1)과 2)를 더 한 숫자에 N을 더 한 숫자가 
#    10으로 나눴을 때 나눠 떨어지면 유효한 숫자입니다. 

T = int(input())

for t in range(1, T+1):
    card_num = list(map(int, input().split()))
    jjak = 0
    hole = 0
    for i in range(len(card_num)): # 0 ~ 15
        if i % 2 == 0:
            hole += card_num[i]*2 # 홀수일때는 2를 곱해서 합산
        elif i % 2 == 1:
            jjak += card_num[i] # 짝수일때는 합산

    digit = (jjak+hole) % 10 # 홀짝값을 더하고 10을 나눈 나머지

    if digit == 0: # 나누어 떨어진 경우
        result = 0 
    else:          # 나누어 떨어지지 않은경우
        result = 10 - digit # 10에 나머지를 뺀다

    print("#{} {}".format(t, result))

# 07.29 22:27 수정
#     T = int(input())

# for i in range(1, T+1):
#     card = list(map(int, input().split()))
#     hole = 0
#     jjak = 0
#     for num in range(len(card)):
#         if num % 2 == 0:
#             hole += card[num]*2
#         elif num % 2 == 1:
#             jjak += card[num]
#     print(hole, jjak)
#     digit = (hole+jjak) % 10

#     if digit == 0:
#         result = 0
#     else:
#         result = 10 - digit
    
#     print("#{} {}".format(i, result))