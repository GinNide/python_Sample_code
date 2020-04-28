age = 'Use other people\'s hearts to play mahjong opposite wanda 1269566 '
# startswith
print(age.startswith('Use'))
# 判断字符串是不是以某个字符开头的

# endwith
print(age.endswith('wanda'))
# 判断字符串是不是以某个字符结尾的


# isalpha() : 字母   判断字符串是不是以字母构成的    不是就返回false
print(age.isalpha())


# isdigit()  : 数字   判断字符串是不是以数字构成的       不是就返回false
print(age.isdigit())

# isalnum()    数字和字符的组合    不是就返回false
print(age.isalnum())

# isspace( )   判断空白      不是就返回false
print(age.isspace())