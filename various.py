def rev(myString):

    strList = list(myString)
    newList = []
    for i in range(len(strList)):
        i = -(i + 1)
        newList.append(str(list(strList[i])))
    revString = ''.join(newList)
    return revString

print(rev("magdalena"))


def rever(x):
    output = ""
    for c in x:
        output = c + output

    return output

print(rever("magda"))