from collections import deque


def can_be_poly(word: str) -> bool:
    deque_word = deque(word)
    while len(deque_word) > 1:
        if deque_word.popleft() != deque_word.pop():
            return False
    return True


if __name__ == '__main__':
    print(can_be_poly(word='abcba'))
    print(can_be_poly(word='abbbc'))

# зачет!
