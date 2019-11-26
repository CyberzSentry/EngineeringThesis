import json

filePath = 'C:\\Projects\\Thesis\Code\\tests\\mailDump_100.json'

with open(filePath, 'r') as file:
    data = json.load(file, encoding='utf-8')

    i = 0
    for message in  data['messages']:
        i+=1
        if i > 10:
            break
        print('-----------------------------------------------',message['id'], '----------------------------------------------\n')
        print(message['content'])
        print()
    