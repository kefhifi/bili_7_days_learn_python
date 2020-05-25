# 函数可以赋值给一个变量
# 函数的返回值可以是一个函数
# 闭包记住了上一次调用的状态！！！！！！

origin = 0
def first(pos):
#    pos = origin
    def sec(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return pos
    return sec

f=first(origin)
print(f(2))
print(f(3))
print(f(5))



