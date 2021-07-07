n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#or we can write it as:

#n = int(input())
#if n % 2 == 1:
    #print("Weird")
#else:
    #if 2 <= n <=5:
    #print('not weird')
#elif 6 <= n <= 20:
    #print("Weird")
#else:
    #print("Not Weird")
