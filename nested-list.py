def check_second_score(list_input, i):
    if (i == 1):
        if (list_input[0][1] == list_input[i][1]):
            i = i + 1
            return (check_second_score(list_input, i))
        else:
            return int(i)
    else:
        if (list_input[i - 1][1] == list_input[i][1]):
            i = i + 1
            return (check_second_score(list_input, i))
        else:
            return int(i)


def evaluate_score(input_list):
    input_list.sort(key=lambda x: x[1])
    x = check_second_score(input_list, 1)
    if ((x!=len(input_list)-1) and (input_list[x][1] == input_list[x + 1][1])):
        temp = list();
        temp.append(input_list[x][0])
        temp.append(input_list[x + 1][0])
        temp.sort()
        for ele in temp:
            print(ele)
    else:
        print(input_list[x][0])


if __name__ == '__main__':
    count = int(input())
    main_list = list()
    for x in range(0, count):
        name = input()
        score = float(input())
        ls = list()
        ls.append(name)
        ls.append(score)
        main_list.append(ls)
    evaluate_score(main_list)
