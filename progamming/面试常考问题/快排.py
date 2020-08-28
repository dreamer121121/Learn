array = [2,3,4,6,0,1,5]
quick_sort = lambda array:array if len(array) <= 1 else quick_sort([num for num in array[1:] if num < array[0]])+[array[0]]+quick_sort([num for num in array[1:] if num >= array[0]])
print(quick_sort(array))
