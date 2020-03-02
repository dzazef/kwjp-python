def remove_duplicates(val_list):
    i = 0
    while i < len(val_list):
        elem = val_list[i]
        j = i + 1
        while j < len(val_list):
            if val_list[j] == elem:
                val_list.pop(j)
                j -= 1
            j += 1
        i += 1
    return val_list


list1 = [1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 4, 4, 4, 0]
print(remove_duplicates(list1))
