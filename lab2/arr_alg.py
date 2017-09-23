def arr_min(arr):
    min=arr[0]
    for elem in arr:
        if elem<min:
            min=elem
    return min


def arr_avg(arr):        
        count=len(arr)
        summ = sum(elem for elem in arr)
        return summ/count
        
arr = [1, 2, 4, 6, 0]

print("minimum")
print(arr_min(arr))

print("average")
print(arr_avg(arr))
