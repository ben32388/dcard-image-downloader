
# f = open('aaaa.txt', 'w+')
# f.write('a')
# f.close()
# content = f.read()
# print(content)

# + 就是如果沒有這個檔就建立
# 在離開with這個區塊就會關檔
with open('aaaa.txt', 'w+') as f:
    f.write('a')
    f.write('a')
    f.write('a')
