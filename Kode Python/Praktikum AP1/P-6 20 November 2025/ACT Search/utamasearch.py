#Data search list
import searching

data1 = [1,3,4,6,7,4,9,10,2,5,8,11]
data2 = [1,7,8,9,10,11,13,16,22,23,24,56]

print(f"Data 1 : {data1}")
print(f"Data 2 : {data2}\n")

index1 = searching.linear_search(data1,7)
index2 = searching.binary_search(data2,23)

print(f"Hasil linear search Data 1 bernilai 7  : di index ke {index1}")
print(f"Hasil binary search Data 2 bernilai 23 : di index ke {index2}")

