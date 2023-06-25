list_a = [1,2,3]
list_b = [3,4]
print(list_a + list_b)

list_c = [1,2,3,4]
list_c[2:2] = [9,9]
print(list_c)
list_d = [1,2,3,4]
list_d[2:4] = [9,9]
print(list_d)
list_e = [1,2,3,4]
del list_e[2]
print(list_e)
del list_d[2:4]
print(list_d)
print(list_d[::-1])
print(list_d[:])
