# Printing list values

vals = [2, 1, 31, 7, 5, 12, 8]

print( vals[ 0 ] )
print( vals[ -2 ] )
print( vals[ 3 ] )
print( vals[1 + 2])
print( vals[9-3])
print( vals[11//2])

nums = []
nums.append(34)
print(nums)
nums.append(99)
print(nums)
nums.insert(0,21)
print(nums)
nums.insert(-1,57)
print(nums)

coworkers = ["Sarah","Matt","Sophie"]
coworkers.remove("Sarah")
print(coworkers)

nums = []
nums.append(34)
nums.insert(0,99)
nums.remove(34)
nums.insert(1,7)
nums.append(3)
nums.remove(7)
print(nums)

coworkers = ["Sarah","Matt","Sophie"]
print(coworkers.pop(1))
print(coworkers)

nums = []
nums.append(34)
nums.insert(0,5)
nums.remove(34)
nums.insert(1,7)
nums.append(3)
nums.pop(2)
print(nums)

print(len(nums))

# Processing lists with loops
myList = []
for num in range(5):
    myList.append(num)

print(myList)

myList = [56,65,98,2,25]
for num in myList:
    print(num)
total = 0
for num in myList:
    total += num

print(total)

def go( vals ):
    #write the code to sum all the values
    y = 0
    for i in vals:
        y += i
    return y

list =[21,16,12,27,36,-10,2]
print(go(list))

# Tuple - a list that CANNOT be changed (edited)
myTuple = (255,0,89)
print(myTuple)
print(myTuple[2])
myTuple.append(33)