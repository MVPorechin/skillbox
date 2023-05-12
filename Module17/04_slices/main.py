alphabet = 'abcdefg'

copy_alphabet = alphabet[:]
print(f'1: {copy_alphabet}')
reverse_alphabet = alphabet[::-1]
print(f'2: {reverse_alphabet}')
every_two_index_alphabet = alphabet[::2]
print(f'3: {every_two_index_alphabet}')
every_two_index_after_first_alphabet = alphabet[1::2]
print(f'4: {every_two_index_after_first_alphabet}')
all_index_before_second_alphabet = alphabet[:1]
print(f'5: {all_index_before_second_alphabet}')
all_index_after_end_alphabet = alphabet[:-2:-1]
print(f'6: {all_index_after_end_alphabet}')
all_index_3_4_alphabet = alphabet[3:4]
print(f'7: {all_index_3_4_alphabet}')
last_3_index_alphabet = alphabet[len(alphabet) - 3:]
print(f'8: {last_3_index_alphabet}')
all_index_in3_4_alphabet = alphabet[3:5]
print(f'9: {all_index_in3_4_alphabet}')
all_index_in3_4_reverse_alphabet = alphabet[4:2:-1]
print(f'10: {all_index_in3_4_reverse_alphabet}')

# зачет!
