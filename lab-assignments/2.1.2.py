
# 1. Create an empty dictionary and display it
my_dict = {}
print("Empty Dictionary:", my_dict)

# 2. Ask the user how many items to add, then input key-value pairs
size = int(input("Number of items: "))
for _ in range(size):
	key = input("key: ")
	value = input("value: ")
	my_dict[key] = value

# 3. Show the dictionary after adding items
print("Dictionary:", my_dict)

# 4. Update a key's value
key_to_update = input("Enter the key to update: ")
if key_to_update in my_dict:
	new_value = input("Enter the new value: ")
	my_dict[key_to_update] = new_value
	print("Value updated")
else:
	print("Key not found")



# 5. Retrieve and print a value using a key
key_to_access = input("Enter the key to retrieve: ")
if key_to_access in my_dict:
	print(f"Key: {key_to_access}, Value: {my_dict[key_to_access]}")
else:
	print("Key not found")



# 6. Use `get()` to retrieve a value
key_to_get = input("Enter the key to get using the get() method: ")
value = my_dict.get(key_to_get)
if value:
	print(f"Key: {key_to_get}, Value: {value}")
else:
	print("Key not found")



# 7. Delete a key-value pair
key_to_delete = input("Enter the key to delete: ")
if key_to_delete in my_dict:
	del my_dict[key_to_delete]
	print("Deleted")
else:
	print("Key not found")



# 8. Display the updated dictionary
print("Updated Dictionary:", my_dict)

