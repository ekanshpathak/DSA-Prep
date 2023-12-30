# Toggle Uppercase to Lower and vice-versa


A = 'eKANSH pATHAK'

a_list = [*A]
for i in range(len(a_list)):
    if ord(a_list[i])>=97 & ord(a_list[i])<=122:
        a_list[i] = chr(ord(a_list[i])-32)
    elif ord(a_list[i])>=65 & ord(a_list[i])<=90:
        a_list[i] = chr(ord(a_list[i])+32)

print(a_list)



print(ord('+'))
