if __name__ == '__main__':
    n = int(input())
    ls=list(input().split(' '))
    ls=ls[:n]
    input_tuple=()
    input_tuple=tuple([int(i) for i in ls])
    print(hash(input_tuple))





