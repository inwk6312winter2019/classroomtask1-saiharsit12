import os

for i, j, k in os.walk('.'):
	for f in k:
		print(f)
