

def concat_lists(list1, list2=[]):
    list2 = list2 if list2 else [ ]:
    list2 += [0]
    return list1 + list2
