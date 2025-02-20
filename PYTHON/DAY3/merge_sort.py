def merge(numbers,low,mid,high):
    array1 = numbers[low:mid]
    array2 = numbers[mid+1:high]

    merged_array = []
    k = 0
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1 
        else: 
            merged_array.append(array1[j])
            j += 1
    merged_array += array1[i:]
    merged_array += array2[j:]


def merge_sort(numbers,low,high):
    if low < high:
        mid = (low + (high - low) // 2)
        merge_sort(numbers,low,mid)
        merge_sort(numbers,mid+1,high)
        sorted_array = merge(numbers,low,mid,high)


print('Enter the input numbers : ')
numbers = [int(num) for num in input().split()]

merge_sort(numbers,0,len(numbers)-1)
print('Sorted Numbers are : ', numbers)