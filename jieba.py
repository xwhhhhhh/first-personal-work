import jieba
import json

item = open('comment.txt', 'r', encoding='utf-8').read()

words = jieba.lcut(item)
word_counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        word_counts[word] = word_counts.get(word, 0) + 1
items = list(word_counts.items())
items.sort(key=lambda x: x[1], reverse=True)

new_list = []
for i in range(len(items)):
    result = {}
    word, count = items[i]
    if count >= 10:
        result['name'] = word
        result['value'] = count
        new_list.append(result)
        
data = {}
data['data'] = new_list
print(data)
with open('comments.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)