
def get_max_value_for(target_list):

    if not target_list: # means, 'if target_list is empty:'
        return max(target_list)
    result = []
    if len(target_list)==1:
        return target_list

    for e in target_list:
        if not isinstance(e, list): # e is not a list
            result.append(e)
        if isinstance(e, list):
            result.extend(get_max_value_for(e))
    anotherlist=max(result)
    print(anotherlist)
    return result






list1 = [7, 9, [12, 5, [30, 15], 17], 7]
print((get_max_value_for(list1)))# 30