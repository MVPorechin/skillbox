def sequence(cnt_card: int, cowboy_card: list, win_card: list) -> str:

    for index in range(cnt_card):
        if cowboy_card[index] != win_card[index]:
            for j in range(cnt_card -1, 0, -1):
                if cowboy_card[j] != win_card[j]:
                    return "NO"
    return "YES"


n = int(input())
cowboy = list(map(int, input().split()))
win = list(map(int, input().split()))


result = sequence(cnt_card=n, cowboy_card=cowboy, win_card=win)
print(result)
