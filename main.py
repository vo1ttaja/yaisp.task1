def join_lists(list_1, list_2):
    join_list = list_1
    for i in range(len(list_2)):
        join_list.append(list_2[i])
    return join_list


def sort_list(list):
    i = len(list) - 1
    swap = True
    while i > 0:
        swap = False
        for j in range(0, i, 1):
            if list[j] > list[j+1]:
                num = list[j+1]
                list[j+1] = list[j]
                list[j] = num
                swap = True
        if not swap:
            break
        i -= 1
    return list

a = [3, 9, 2, 7]
b = [8, 3, 5]
new_list = join_lists(a, b)
final_list = sort_list(new_list)
print(final_list)

