# 全局变量 函数体内外都能返回这个变量
a = 100  # 全局变量
def testa():
    print(a)
def testb():
    print(a)

testa()
testb()