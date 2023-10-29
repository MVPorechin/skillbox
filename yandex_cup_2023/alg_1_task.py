def cat_art(cnt: int, picture: list) -> int:
    slow = 0
    speed = 1
    cnt_section = 0
    if picture[slow] > 1:
        return 0
    for _ in range(2, len(picture)):
        if picture[slow] + 1 == picture[speed]:
            cnt_section += 1
        speed += 1
        slow += 1

    return cnt_section


res = cat_art(cnt=5, picture=[1, 2, 3, 2, 3])
print(res)

