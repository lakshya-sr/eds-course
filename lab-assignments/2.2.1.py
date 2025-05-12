data = list(map(int, input().split()))
element = int(input())

if element in data:
	print(data.index(element))
else:
	print("Not found")
