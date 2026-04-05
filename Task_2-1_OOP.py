file_names = ['1.txt', '2.txt', '3.txt']  # список всех файлов
all_text = []
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        all_text.append({
            'name': file_name,
            'line_count': len(content),
            'content': content
        })
sort_lst = sorted(all_text, key=lambda x: x['line_count'])
with open('result_file.txt', 'w', encoding='utf-8') as file_result:
    for info in sort_lst:
        file_result.write(info['name'] + '\n')
        file_result.write(str(info['line_count']) + '\n')
        file_result.writelines(info['content'])
        file_result.write('\n')

#Вместо открывания каждого файла цикл, который перебирает список файлов, т.к количество
# файлов может быть огромное и для каждого не напишешь открытие и словарь