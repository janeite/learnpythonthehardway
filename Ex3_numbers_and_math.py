#coding=UTF-8
print "I will now count my chickens:"

print "Hens",25+30/6#=25+5=30
print "Roosters",100-25*3%4#=100-75%4=100-3=97 %为取余

print  "Now I will count the eggs:"

print 3+2+1-5+4%2-1/4+6#=3+2+1-5+0-0+6=7 1/4取整为0

print "Is it true that 3+2<5-7?"

print 3+2<5-7 #运算符号优先级大于比较符号

print "What is 3+2?",3+2
print "What is 5-7?",5-7

print "Oh,that's why it's False."

print "How about some more."

print "Is it greater?",5>-2 #比较符号输出值为True/False
print "Is it greater or equal?",5>=-2
print "Is it less or equal?",5<=-2

print "Now Let's count again more accurate:"

print "Hens",25.0+30.0/6 #算式中有一个浮点数就可以输出浮点数结果
print "Roosters",100.0-25.0*3%4

print  "Now I will count the eggs:"

print 3.0+2+1-5+4.0%2-1.0/4+6
#添加任意浮点数只能输出7.0，只有将1/4部分改为浮点才能输出6.75
#整数相除向下取整，如：7/4输出1，7.0/4输出1.75，-7/4输出-2

print "Is it true that 3+2<5-7?"

print 3.0+2<5.0-7 #运算符号优先级大于比较符号

print "What is 3+2?",3+2.0
print "What is 5-7?",5-7.0

print "Oh,that's why it's False."

print "How about some more."

print "Is it greater?",5/2>2 #整形取整后才比较大小
print "Is it equal?",5/2==2.5 #比较符号一侧出现浮点数并不会影响另一侧取整
print "Is it less or equal?",5/2.0<=2.1
