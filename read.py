data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('The files are being process. No of data is', len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('Average is', sum_len/len(data))
