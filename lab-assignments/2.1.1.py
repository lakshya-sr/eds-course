# write the code..
array = []
while True:
	print("1. Add\n2. Remove\n3. Display\n4. Quit")
	action = input("Enter choice: ")
	if action == "1":
		try:
			n = int(input("Integer: "))
			array.append(n)
			print("List after adding:", array)
		except ValueError:
			print("Invalid input")
	elif action == "2":
		if len(array) == 0:
			print("List is empty")
		else:
			n = int(input("Integer: "))
			try:
				i = array.index(n)
				del array[i]
				print("List after removing:", array)
			except ValueError:
				print("Element not found")
	elif action == "3":
		if len(array) > 0:
			print(array)
		else:
			print("List is empty")
	elif action == "4":
		break
	else:
		print("Invalid choice")
	
