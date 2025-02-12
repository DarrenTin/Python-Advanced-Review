import array

arr = array.array('i', [i for i in range(1, 100)])
print(arr[75])
arr.append(101)
arr.insert(99, 100)
arr.remove(101)
print(arr)
