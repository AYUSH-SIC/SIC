import json

def bubble_sort(array):
    s = serialize(array)
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

def optimized_bubble_sort(array):
    s = serialize(array)
    for i in range(len(array)-1):
        sorted = True
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
                sorted =False
            if sorted:
                return
            
def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return json.dumps(formatted)

arr = [9,8,7,5,4,2,6,2,89]

s = serialize(arr)

bubble_sort(arr)