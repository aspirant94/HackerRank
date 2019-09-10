if __name__ == '__main__':
    N = int(input())
    insert_values = []

    for _ in range(N):
        operation,*values=input().split(' ')
        if(operation == 'insert'):
            ls=list(map(int,values))
            insert_values.insert(ls[0],ls[1])
        if(operation == 'print'):
            print(insert_values)
        if(operation == 'remove'):
            ls = list(map(int, values))
            insert_values.remove(ls[0])
        if (operation == 'append'):
            ls = list(map(int, values))
            insert_values.append(ls[0])
        if(operation == 'sort'):
            insert_values.sort()
        if (operation == 'pop'):
            insert_values.pop()
        if (operation == 'reverse'):
            insert_values.reverse()

