def locals():
    print('locals开始')
    print('locals结束')

def text():
    print('-------------test start------------')
    print('程序开始执行')
    locals()   # locale 要调用 先定义
    print('程序结束')

text()