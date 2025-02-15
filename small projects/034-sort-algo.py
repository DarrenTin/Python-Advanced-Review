def bubble_sort(arr):  # Fixed Bubble Sort
    count = 1
    n = len(arr)
    for h in range(n - 1):  # Run n-1 passes
        for i in range(n - h - 1):  # Reduce comparisons after each pass
            if arr[i] > arr[i + 1]:
                print('operation', count, '=>', arr[i], arr[i + 1], '->', arr[i + 1], arr[i])
                count += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def selection_sort(arr):  # Fixed Selection Sort
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the minimum element with the first unsorted element
        print(arr)
        print('--------')
    return arr

def insertion_sort(arr):  # Fixed Insertion Sort
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position
    return arr

def merge_sort(arr):  # Completed Merge Sort
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):  # Completed Quick Sort
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [7, 6, 3, 2, 5, 4, 9, 8, 3]
# print(bubble_sort(arr))
# print(selection_sort(arr))
print(insertion_sort(arr))