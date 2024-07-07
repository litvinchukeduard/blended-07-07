# ['a', 'b', 'c', 'd', 'c'] [1, 2, 3, 4] -> ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'c']
def my_zip_add_element(list_one: list, list_two: list) -> list:
    maximal_list_length = 0
    if len(list_one) > len(list_two):
        maximal_list_length = len(list_one)
    else:
        maximal_list_length = len(list_two)

    result_list = []
    for i in range(0, maximal_list_length):
        # print(i)
        if i < len(list_one):
            result_list.append(list_one[i])
        if i < len(list_two):
            result_list.append(list_two[i])
    return result_list

list_one = ['a', 'b', 'c', 'd', 'e']
list_two = [1, 2, 3, 4]
print(my_zip_add_element(list_one, list_two))