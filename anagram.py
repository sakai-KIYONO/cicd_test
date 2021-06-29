def is_anagram(arg1, arg2):

    if type(arg1) != str or type(arg2) != str:
        raise ValueError

    list1 = list(arg1)
    list2 = list(arg2)

    if set(list2) == set(list1) and len(arg1) == len(arg2):
        print(list1)
        print(list2)
        return True
    return False

#if __name__ == '__main__':
#    is_anagram('Some String', 1)
