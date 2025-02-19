def partitionArray(numbers,low,high):
    j = low
    pivot = numbers[high]
    for i in range(low,high):
        if numbers[i] < pivot:
            numbers[i],numbers[j] = numbers[j],numbers[i]
            j += 1
    numbers[j],numbers[high] = numbers[high],numbers[j]
    return j

def quickSort(numbers,low,high):
    if low < high:
        pivot_index = partitionArray(numbers,low,high)
        quickSort(numbers,low,pivot_index-1)
        quickSort(numbers,pivot_index+1,high)
