
#Part A
weeks = 16
print(weeks, type(weeks))
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(classes_per_week, type(classes_per_week))
print("Cost per week:", cost_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class, type(cost_per_class))
print("Cost per class:",cost_per_class)



#Part B
import random
my_list = ["green", "red", "pink", "blue", "yellow"]
var = random.choice(my_list)
print(var)