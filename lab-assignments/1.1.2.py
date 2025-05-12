n = int(input())


if n < 10:
	print(n**2)
elif n < 100:
	print("%.2f" % round(n**(1/2), 2))
elif n < 1000:
	print("%.2f" % round(n**(1/3), 2))
else:
	print("Invalid")
