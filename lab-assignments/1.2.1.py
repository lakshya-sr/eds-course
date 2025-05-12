
n = int(input())
marks = [int(i) for i in input().split()]
fail = False
for m in marks:
	if m < 40:
		print("Fail")
		fail = True
		break
if not fail:
	agg_percent = sum(marks)/n
	print("Aggregate Percentage: ", end="")
	if agg_percent >= 75:
		print("%.2f" % agg_percent)
		print("Grade: Distinction")
	elif agg_percent >= 60:
		print("%.2f" % agg_percent)
		print("Grade: First Division")
	elif agg_percent >= 50:
		print("%.2f" % agg_percent)
		print("Grade: Second Division")
	elif agg_percent >= 40:
		print("%.2f" % agg_percent)
		print("Grade: Third Division")
	
