import json

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

a=[9,7,7,3,6,2,4,2,4,8]

serialized = serialize(a)
n=len(a)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)