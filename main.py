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


def read_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            line = file.readline().strip()
            out_list = list(map(int, line.split(", ")))
            return out_list
    except FileNotFoundError:
        print("Файл " + file_path + " не найден.")
    except ValueError:
        print("Не все элементы являются целыми числами.")
    except Exception as e:
        print("Произошла ошибка: " + e)


def list_to_str(list):
    str0 = ""
    for i in range(len(list) - 1):
        str0 += str(list[i]) + ", "
    str0 += str(list[-1])
    return str0


list1 = read_from_file("tests/testInputFile1.txt")
list2 = read_from_file("tests/testInputFile2.txt")
new_list = join_lists(list1, list2)
final_list = sort_list(new_list)
with open("outputFile.txt", "w") as file:
    final_str = list_to_str(final_list)
    file.write(final_str)
