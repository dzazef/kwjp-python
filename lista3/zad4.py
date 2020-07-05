

def qsort(list_):
    """QuickSort using filter"""
    if len(list_) > 1:
        pivot = list_.pop(int(len(list_) / 2))
        return (qsort(list(filter(lambda x: x < pivot, list_))) + [pivot] +
                qsort(list(filter(lambda x: x >= pivot, list_))))
    else:
        return list_


print(qsort([-6, -8]))
