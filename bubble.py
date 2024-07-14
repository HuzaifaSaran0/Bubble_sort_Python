arr = [1,4,2,7,5,9]
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
