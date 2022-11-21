#Write a program that calculates the number of packages of hot dogs 
#the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.
import math
#The program should ask the user for the number of people attending the cookout 
people_attending= int(input("How many people are attending? "))
# the number of hot dogs each person will be given.
hotdog_given = int(input("How many hotdogs will each person receive? "))

#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.
hotdog_package = 10
hotdog_buns_package = 8
 #calculation 


#The program should display the following details:
total__hotdogs = people_attending * hotdog_given 
#print ("Total Hotdogs is ", total__hotdogs)
 
# The minimum number of packages of hot dogs required
min_hotdog_package =  total__hotdogs / hotdog_package #
#print ("Total Hotdog package", hotdog_package)

# The minimum number of packages of hot dog buns required
min_hotdog_buns = total__hotdogs / hotdog_buns_package
#print("Min buns needed", hotdog_buns)

# The number of hot dogs that will be left over
hotdog_leftover = total__hotdogs % hotdog_package 
#print ("Leftover Hotdog" , hotdog_leftover)

# The number of hot dog buns that will be left over
buns_lefover = total__hotdogs % hotdog_buns_package
#print("Buns leftover", buns_lefover,)

 

print(f"Hotdog needed is: {total__hotdogs}")
print(f"Min Hotdog packages needed is: {math.ceil(min_hotdog_package)}")
print(f"Min Hotdog buns needed is: {math.ceil(min_hotdog_buns)}")
print(f"Hotdog left over: {math.ceil(hotdog_leftover) }")
print(f"Hotdog buns left over:{math.ceil(buns_lefover)}")