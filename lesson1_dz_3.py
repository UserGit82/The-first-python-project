for i in range(100):
    my_str = str(i + 1)
    my_list = list(my_str)
    if int(my_list[-1]) == 1 and i + 1 != 11:
        print(f'{i+1} процент')
    elif int(my_list[-1]) > 1 and int(my_list[-1]) <= 4:
        if  i + 1 > 10 and i + 1 <= 14:
            print(f'{i+1} процентов')
        else:
            print(f'{i+1} процента')
    else:
        print(f'{i+1} процентов')