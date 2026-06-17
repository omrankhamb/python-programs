# Sortin fictionaire

dic = {
    'name' : 'omprasad',
    'name2' : 'soham',
    'name3' : 'harsh'
}


def DictSortByvalues(dic : dict )->dict:
    lis = []

    for i in dic.values():
        lis.append(i)

    lis.sort()

    count = 0
    for i in dic.keys():
        dic[i] = lis[count]
        count+=1
    return dic

DictSortByvalues(dic)