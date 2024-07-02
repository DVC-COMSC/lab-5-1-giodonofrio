def getinput():
    num = int(input("Enter a number: "))
    return num


def getsum(v1, v2):
    sum = v1 + v2
    return sum


def printval(v1, v2, total):
    print("First value: ", v1)
    print("Second value: ", v2)
    print("Total: ", total)


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
