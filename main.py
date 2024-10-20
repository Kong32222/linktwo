'''

'''
#输入明文
text = input('请输入明文:')

#凯撒加密
s = ''
for c in text:
    if 'a' <= c <= 'w' or 'A' <= c <= 'W':
        c = chr(ord(c) + 3)
    elif 'x' <= c <= 'z' or 'X' <= c <= 'Z':
        c = chr(ord(c) - 23)
    elif '0' <= c <= '9':  
        c = chr((ord(c) + 3)) 
    s = s + c
    
#输出密文 
print('输出密文:' + s)
