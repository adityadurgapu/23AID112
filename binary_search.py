def binary_search(list,item):
    low = 0
    high  = len(list) - 1

    while low <= high:
        mid = (high - low //2)
        guess = list[mid]

        if guess == item :
            return mid
        
        if item > guess:
            low = mid + 1

        else:
            high = mid -1
    return None


lists = [1,5,8,9,15,17]
print(binary_search(lists,15))