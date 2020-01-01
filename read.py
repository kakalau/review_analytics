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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are',len(new), 'data len is less than 100')
print(new[0])
print(new[1])