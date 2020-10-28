data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

print(data[0])

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)

# good = [d for d in data if 'good' in d ]
print('一共有', len(good), '筆留言提到good')
print(good[0])
print(good[1])

#文字計數

wc = {} #word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc: #如果word有出現在wc裡
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key進wc字典

for word in wc: #讀取wc字典中的每一個key
    if wc[word] > 100:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('請問想查什麼字')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else:
        print('這個字沒有出現過喔!')
        
print('感謝使用本查詢功能')

