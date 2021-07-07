# take input
n = int(input('how many? '))
#number of list
#numbers seperate by space
#convert list() to set(), to reverse duplicates
arr = set(map(int, input('scores here: ').split(' ')))
sortedNumber = [numbers.pop()]

print(number)
print(sortedNumber)

for num in numbers:
    index = 0
    while(index < len(sortedNumber) and num > sortedNumber[index]):
        index = index + 1
    sortedNumber.insert(index, num)
    #[32,4].insert[1, 5] ==> [32, 5, 4]
    # sortedNunmber[index] ==> sortedNumber[0]
    #print(sortedNumber)
print(sortedNumber)

if(len(sortedNumber) <= 1):
    print('Runnerup score is:', sortedNumber[1])
else:
    print('Runnerup score is:', sortedNumber[0])




n = int(input())
arr = map(int, input().split())
number = set(arr)
sortedNumber = [number.pop()]

for num in number:
    index = 0
    while(index < len(sortedNumber) and num > sortedNumber[index]):
        index = index + 1
    sortedNumber.insert(index, num)

if(len(sortedNumber) <= 1):
    print('Runnerup score is:', sortedNumber[1])
else:
    print(sortedNumber[-2])






# sort and store into list()

# take