# coding=utf-8
#字符串x中插入数字10
x="There are %d types of people." % 10
binary="binary"
do_not="don't"
#字符串y中插入两个字符串：binary和do_not
y="Those who know %s and those who %s." % (binary,do_not)

print x
print y
# print命令后的字符串中插入字符串x，%r输出字符串时保留x两侧的引号。
print "I said: %r." % x
# print命令后的字符串中插入字符串y
print "I also said: '%s'." % y

hilarious =False
joke_evaluation="Isn't that joke so funny?! %r"
# 字符串joke_evaluation中插入值hilarious，后者不是字符串，所以输出的时候没有引号。
print joke_evaluation % hilarious

w="This is the left side of ... "
e="a string with a right side."
# 用加号连接两个字符串，也可以用逗号连接
print w + e
