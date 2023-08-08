import os

path = "D:\soft"


def read_from_files_write_to_file(path:str) -> str:
    list_files = os.listdir(path)
    one_file = 'D:\one_file.txt'
    with open(file=one_file, mode='a', encoding='ISO-8859-1') as one_f:
        for file in list_files:
            abs_path = path + "\\" + file
            one_f.writelines(str(file)+'\n')
            with open(file=abs_path, mode='r', encoding='ISO-8859-1') as txt:
                for line in txt:

                    one_f.writelines(str(line))


read_from_files_write_to_file(path=path,)





