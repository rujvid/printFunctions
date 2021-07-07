dataList = []
N = int(input())
for i in range(N):
    commandInput = input('enter command here: '.split(" ")
    command = commandInput.split()[0]

    if (command == 'insert'):
        pos = int(commandInout[1])
        ele = int(commandInput[2])
        dataList.insert(pos, ele)
    elif command == 'print':
        print(dataList)
    elif command == 'pop':
        dataList.pop()
        print('after pop(): ', dataList)

    # for x in range(N):
    # commandStart = list(input().split(" "))
    # commandWords = commandStart[0]

    elif commandWords == "insert":
    index = int(commandStart[1])
    value = int(commandStart[2])
    try:
        dataList.insert(index, value)
    except ValueError:
        continue

    elif commandWords == "print":
    print(dataList)

    elif commandWords == "remove":
    value = int(commandStart[1])
    try:
        dataList.remove(value)
    except ValueError:
        continue

    elif commandWords == "append":
    value = int(commandStart[1])
    try:
        dataList.append(value)
    except ValueError:
        continue

    elif commandWords == "sort":
    value = commandStart[0]
    try:
        dataList.sort()
    except ValueError:
        continue

    elif commandWords == "pop":
    value = commandStart[-1]
    try:
        dataList.pop()
    except ValueError:
        continue

    elif commandWords == "reverse":
    value = commandStart[0]
    try:
        dataList.reverse()
    except ValueError:
        continue