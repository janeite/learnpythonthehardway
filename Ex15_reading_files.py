#coding=UTF-8
#导入sys中的参数
#from sys import argv
#分解两个参数
#script,filename = argv
#函数open(文件名，打开权限)
#txt = open(filename)

#print "Here is your file %r:" % filename
#read()读出文件内容
#print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
