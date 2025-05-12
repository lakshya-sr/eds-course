import pandas as pd
from itertools import combinations
from collections import Counter

file_name = input()

df = pd.read_csv(file_name)

grouped = df.groupby('Date')['Product'].apply(list)

pair_counter = Counter()

for products in grouped:
	for pair in combinations(sorted(set(products)), 2):
		pair_counter[pair] += 1

if pair_counter:
	max_count = max(pair_counter.values())

	most_frequent_pairs = [pair for pair, count in pair_counter.items() if count == max_count]

	for pair in most_frequent_pairs:
		print(f"{pair[0]} and {pair[1]}: {max_count} times")

else:
	print("No product pairs found.")
