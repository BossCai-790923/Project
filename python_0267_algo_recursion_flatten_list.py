def flatten_list(target_list):

    # base case
    # if target_list is False (meaning target_list is empty) -> not target_list is True
    # when target_list is empty, target_list == False

    if not target_list: # means, 'if target_list is empty:'
        return target_list

    # recursive call
    result = []

    for e in target_list:

        if not isinstance(e, list): # e is not a list
            result.append(e)
        if isinstance(e, list):
            result.extend(flatten_list(e))


    return result




list1 = [1, [2, [3, [4, 5]]]]
result = flatten_list(list1) # [1, 2, 3, 4, 5]
print(result)