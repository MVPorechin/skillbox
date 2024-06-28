from typing import Dict, Any
from collections import Counter


def count_unique_characters(msg: str) -> int:
    unique: Dict[Any, int] = Counter(list(map(lambda word: word.strip(), msg.lower().strip())))
    return sum(list(map(lambda value: value == 1, unique.values())))


if __name__ == '__main__':
    message = "Today is a beautiful day! The sun is shining and the birds are singing."

    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)

# зачет!
