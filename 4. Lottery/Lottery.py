# importing the random and time module
import random
import time

## Lets imagine you have names of employees of your department
## And you want to run a lottery campainge among your department

## In this case, so you created a list of names of your colleagues 
## How to create a list in python?

names = ['Faisal', 'Faezah', 'Fahad', 'Faezah', 'Fahim']
print(names)

## Lets say you forgot to add name of one of your colleage.
## How to append an element in a list?

names.append('Rajon')
#print(names)

## Now you want to see the total number of ppl in the name list
#print(len(names))
##print('No. of ppl in the list are : '+ str(len(names)))

## Lets say you want to add your CEO's name AKA "The Boss"
names.insert(0, "John Snow")
#print(names)

## And GM's name in the list too
names.insert(1, "Sansa")
print(names)

## Let's say you want to remove one of your colleauge's name,
## whom you don't like
names.remove("Rajon")
print(names)

## Let's say, you have a crush in you department and u thought you want to
## add her name one more times.


## Let's say, you want to check the list for duplication
count = names.count('Faezah')
#print(count)

## Let's say, you want to check the list for duplication
names.reverse()
#print(names)

list_duplication_name = []

def checkDup(name):
    return list_duplication_name.count(name)

for name in names:
    if names.count(name) > 1:
        if checkDup(name) == 0:
            list_duplication_name.append(name)

#print(list_duplication_name)

dictNamesWithRandomNumber = {}
tupleRandomNumber = ()

## Random number generation
for name in names:
    #print(name +':'+str(random.randint(0,1000)))
    dictNamesWithRandomNumber[name] = random.randint(0,1000)

print(dictNamesWithRandomNumber)

for value in dictNamesWithRandomNumber.values():
    tupleRandomNumber = (value,)+tupleRandomNumber

print(tupleRandomNumber)
print('\n')
print("And the winner is .....")
time.sleep(5)
print('\n')
print("##################Congratulation#################")

my_elem = random.choice(tupleRandomNumber)
print(my_elem)

# function to return key for any value from dictNamesWithRandomNumber
def get_key(val):
    for key, value in dictNamesWithRandomNumber.items():
         if val == value:
             return key
 
    return "key doesn't exist"

# Print the name of the winner
print("The winner is : " + get_key(my_elem))


## Interesting
a, b, c = [1,2,3]
print(c)
