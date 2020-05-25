import re
a="1C2C++3Python4p&hp5java6hell"

# 找数字
r = re.findall('\d',a)
print(r)

r = re.findall('[0-9]',a)
print(r)
# 找非数字
r = re.findall('\D',a)
print(r)

r = re.findall('[^0-9a-zA-Z_]',a)
print(r)
# [^0-9a-zA-Z_]    \w
# \W 非单词字符

print("...............")
# 函数作为参数的使用
s="A8C3721D86"

def new_c(ch):
    ch_v=ch.group()
    if int(ch_v) >= 6:
        return "9"
    elif int(ch_v) < 6:
        return "0"
    else:
        return ch

r=re.sub("\d",new_c,s)
print(r)


print("...............")
# () 括号用法:分组
s="Life is short, i use Python"
r=re.findall("Life.*Python",s)
print(r)   # ['Life is short, i use Python']
r=re.findall("Life(.*)Python",s)
print(r)  # [' is short, i use ']

s="Life is short, i use Python, i love Python"
r=re.search("Life(.*)Python(.*)Python",s)
print(r.group(0))  # Life is short, i use Python, i love Python   完整的分组
print(r.group(1))  #  is short, i use    第一个分组
print(r.group(2)) # , i love   第二个分组
# 也可以这样用 group
print(r.group(0,1,2)) # ('Life is short, i use Python, i love Python', ' is short, i use ', ', i love ')   是一个元组
# groups  只返回 分组，不包含完整的分组
print(r.groups())  # (' is short, i use ', ', i love ')




