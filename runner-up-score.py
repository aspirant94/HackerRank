from collections import OrderedDict


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(' '))
    ls = list(arr)
    ls= ls[:n]
    ls=list(OrderedDict.fromkeys(ls))
    ls.sort(reverse=True)
    print(ls[1])
