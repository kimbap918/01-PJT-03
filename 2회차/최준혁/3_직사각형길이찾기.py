T = int(input())

for t in range(1, T+1): 
    square = list(input().split()) # 입력받은 값을 리스트에 담는다.
    square.sort() # 리스트를 정렬한다(수 비교를 위해)
    # print(square)
    if square[0] != square[1]: # 리스트의 첫번째와 두번째 숫자가 다르면
        print('#{} {}'.format(t,square[0])) # 첫번째 숫자 출력
    else: # 같다면?
        print('#{} {}'.format(t,square[2])) # 마지막 숫자 출력

# 22.07.29 21:58 수정
# T = int(input())

# for i in range(1, T+1):
#     square = list(input().split())
#     square.sort() 
#     if square[0] != square[1]:
#         print("#{} {}".format(i, square[0]))
#     elif square[0] == square[1]:
#         print("#{} {}".format(i, square[2])) 