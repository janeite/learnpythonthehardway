name = 'Zed A.Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall, which is %d centmeters." % (height, height*2.54)
print "He's %d pounds heavy, which is %d kilograms." % (weight, weight*0.45359237)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age+height+weight)

# more about python format characters, in tutorial/7.1.1.old string formatting
# %d number, %s string, %r string
