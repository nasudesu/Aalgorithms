def combine_list2(list1, list2):
    new_list = list1 + list2
    for i in range(len(new_list)):
        for j in range(i, len(new_list)):
            if new_list[i] > new_list[j]:
                new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list


def combine_lists(list1, list2):
    new_list = []
    i = j = 0
    for _ in range(len(list1) + len(list2)):
        if i >= len(list1) or j < len(list2) and list1[i] > list2[j]:
            new_list.append(list2[j])
            j += 1
        else:
            new_list.append(list1[i])
            i += 1
    return new_list


print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
