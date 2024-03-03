from collections import Counter
n = list(str(input()).upper())
c_result = Counter(n).most_common()
max_num = c_result[0][1]
max_list = []
for word, count in c_result:
    if max_num == count:
        max_list.append(word)
if len(max_list) > 1:
    print('?')
else:
    print(max_list[0])