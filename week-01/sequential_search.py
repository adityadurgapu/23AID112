def seq_search(list,item):
    a = 0
    while a < len(list):
        if  list[a] == item:
            return a

        a += 1
    return None

nums = [45,45,548,6,15]
print(seq_search(nums,548))
print("The number of numbers in the list is :",len(nums))