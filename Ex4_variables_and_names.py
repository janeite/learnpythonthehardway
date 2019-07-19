#How many cars do we have
cars=100
#How many seats in each car
space_in_a_car=4
#How many drivers do we have
drivers=30
#How many passengers
passengers=90
#how many cars is empty
cars_not_driven=cars-drivers
#How many cars have a driver
cars_driven=drivers
#How many passengers we can take
carpool_capacity=cars_driven*space_in_a_car
#How many passengers we put in each car
average_passengers_per_car=passengers/cars_driven


print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"passengers to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
print "Hey %s there."%"you"

#study drills
# the error means we don't defind the variable "car_pool_capacity" before we use it.
# we defind a variable "carpool_capacity", not"car_pool_capacity".
# I think use 4.0 for space_in_a_car is not necessary, because we don't need floating point in this case.
