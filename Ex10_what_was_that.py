tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat
'''
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i
'''
s ="I had \ta little frog, \nhis name was \"Tiny Tim\"."
print "%r" % s
print "%s" % s
# why %r can't print \"
