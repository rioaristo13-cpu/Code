import sorting

data = [5,1,2,5,7,3,10,9,12,11,8,4]

print (f"Data : {data}\n")

ssort = sorting.selection_sort(data)
qsort = sorting.quick_sort(data)

print (f"Hasil Selection Sorting : {ssort}")
print (f"Hasil Quick Sorting : {qsort}")

