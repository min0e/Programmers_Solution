def solution(lottos, win_nums):
    x = lottos.count(0)      #모르는 수의 개수
    cnt = 0                  #같은 수의 개수
    answer = [0, 0]

    for i in lottos :
        if i in win_nums:
            cnt = cnt + 1

    low = 6 - (cnt - 1)       #최저 순위
    if (cnt == 0) : low = 6

    if (x == 0) : high = low  #최고 순위
    elif (cnt + x < 2) : high = 6 
    else : high = low - x
    if (high < 1) : high = 1

    answer[0] = high
    answer[1] = low

    return answer
