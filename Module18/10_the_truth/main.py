import string


def caesar(text, step, alphabets):
    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table).split()


def tab_letters(position_tab, shift_word_list):
    output = []
    for word in shift_word_list:
        result_word = list(word)
        for index in range(position_tab):
            result_word.insert(0, result_word.pop())
        output.append(result_word)
        if '/' in result_word:
            position_tab += 1
            output.append('\n')
        encrypted = ' '.join(''.join(word) for word in output).replace("/", ".").replace("/", ".").replace("(", "`").replace("+", "*").replace("-", ",")
    return encrypted


message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt ' \
          'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp ' \
          'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme ' \
          'wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
          'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc ' \
          'bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
          'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju ' \
          'znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip '

decrypt_caesar = caesar(message, 25, (string.ascii_lowercase, string.ascii_uppercase))
encrypt_caesar = tab_letters(3, decrypt_caesar)
print(f'{encrypt_caesar}')

# зачет!
