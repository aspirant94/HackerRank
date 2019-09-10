if __name__ == '__main__':
    x = input()
    ls=[s.isalnum() for s in x]
    if (True in ls):
        print(True)
    else:
        print(False)

    ls1=[s.isalpha() for s in x]
    if (True in ls1):
        print(True)
    else:
        print(False)

    ls2=[s.isdigit() for s in x]
    if (True in ls2):
        print(True)
    else:
        print(False)

    ls3=[s.islower() for s in x]
    if (True in ls3):
        print(True)
    else:
        print(False)

    ls4=[s.isupper() for s in x]
    if (True in ls4):
        print(True)
    else:
        print(False)




