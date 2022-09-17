# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# aaaaabbbcccc = 5a3b4c

with open('Homework005/task3_decoded.txt', 'r') as data:
    my_text = data.read()


def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in (ss):
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        str_code+=str(count)+prev_char
        return str_code

str_code = encode_rle(my_text)
print(str_code)

with open('Homework005/task3_encoded.txt', 'r') as data:
    my_text2 = data.read()


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print(str_decode)
