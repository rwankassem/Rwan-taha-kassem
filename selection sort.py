#rwan taha kassem
#sec 4

def selection_sort(arr):
  
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)

arr = [52, 18, 2, 67, 3, 0]
selection_sort(arr)
print("sorted array is:", arr)