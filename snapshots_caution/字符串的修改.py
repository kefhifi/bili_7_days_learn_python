
# 方法1：将字符串转换成列表后修改值，然后用join组成新字符串
# 原字符串
s = 'abcdef'
# 将字符串转换为列表
s1 = list(s)
print(s1)
# 将列表中的第5个字符修改为E
s1[4] = 'E'
# 将列表中的第5个字符修改为E
s1[5] = 'F'
print(s1)
# 用空串将列表中的所有字符重新连接为字符串
s = ''.join(s1)
print(s)

# 方法2: 通过字符串序列切片方式
spam = 'I have a pet cat'

spam = spam[:13] + 'C' + spam[14:]
print(spam)

# 方法3: 使用字符串的replace函数
s = 'abcdef'
# 用A替换a
s = s.replace('a', 'A')
print(s)
# 用123替换bcd
s = s.replace('bcd', '123')
print(s)
