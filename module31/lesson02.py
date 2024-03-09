import re


text_2 = 'AV is largest Analytics community of India'
res = re.findall(pattern=r"\b[aeiouAEIOU]\w+", string=text_2)
print(f' {res}')


deep_ocean = """ test text test text test text test text Nenemo test text test text test text 
                    test text test text test text test text nemo test text test text test text
                test text test Nemo text test text test text nemo test text test text test text
                test text test Nemo text test text test text Nnemo0 test text test text test text    
                """

nemo_pattern = r'[Nn]em\w{0,2}'

full_search = re.findall(pattern=nemo_pattern, string=deep_ocean)
print(full_search)

nemo_matched = re.search('Nemo', deep_ocean)
print(nemo_matched)

transparent = re.sub(r'[Oo]\w{4}\s+', '', deep_ocean)
print(transparent)