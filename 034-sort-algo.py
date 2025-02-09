import time
import random

# Sorting algorithms
def bubble_sort(arr):
    """Bubble Sort Algorithm (O(n²))"""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Selection Sort Algorithm (O(n²))"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion Sort Algorithm (O(n²))"""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Merge Sort Algorithm (O(n log n))"""
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

def quick_sort(arr):
    """Quick Sort Algorithm (O(n log n) average, O(n²) worst)"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Dictionary of algorithms
sorting_algorithms = {
    "bubble": (bubble_sort, "O(n²)"),
    "selection": (selection_sort, "O(n²)"),
    "insertion": (insertion_sort, "O(n²)"),
    "merge": (merge_sort, "O(n log n)"),
    "quick": (quick_sort, "O(n log n) average, O(n²) worst"),
}

def custom_sort():
    """User selects sorting algorithm, and program calculates execution time and complexity."""
    print("\n🔢 Available Sorting Algorithms:")
    for name in sorting_algorithms:
        print(f"  - {name.capitalize()} Sort")

    choice = input("\nChoose a sorting algorithm: ").strip().lower()
    
    if choice not in sorting_algorithms:
        print("❌ Invalid choice! Defaulting to Bubble Sort.")
        choice = "bubble"

    sorting_function, complexity = sorting_algorithms[choice]

    # Generate random list
    n = int(input("Enter number of elements to sort: ") or "10")
    data = [random.randint(1, 100) for _ in range(n)]
    print("\n🔢 Unsorted Data:", data)

    # Measure execution time
    start_time = time.time()
    sorted_data = sorting_function(data.copy())  # Copy to avoid modifying original
    end_time = time.time()

    # Display results
    print("\n✅ Sorted Data:", sorted_data)
    print(f"📌 Algorithm: {choice.capitalize()} Sort")
    print(f"📊 Big O Complexity: {complexity}")
    print(f"⏱️ Execution Time: {end_time - start_time:.6f} seconds\n")

# Run the sorting program
if __name__ == "__main__":
    custom_sort()
