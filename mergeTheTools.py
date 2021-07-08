def removeDupes(string):
    result = ""
    for c in string:
        if (result.find(c) == -1):
            result = result + c
    return result


def merge_the_tools(string, k):
    n = len(string)
    parts = []
    index = 0
    while (index < len(string)):
        parts.append(string[index: index + k])
        index = index + k

    # remove duplicates in each part
    for part in parts:
        print(removeDupes(part))


string = 'ABADDDGHIJ' #input()
k = 3 #int(input())
# merge_the_tools(string, k)


