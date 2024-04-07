with open('recipes.txt', 'r', encoding='utf-8') as f:
    fileText = f.read()

def task_three(name_file):
    result = []
    for el in name_file:
        with open(el, 'r', encoding='utf-8') as file:
            text = file.read()
            count_line = text.count('\n') + 1

            result.append({'name': el, 'countLine': count_line, 'text': text})

    result.sort(key=lambda x: x['countLine'])

    with open('taskThree.txt', 'w', encoding='utf-8') as f:
        for el in result:
            name = el['name']
            countLine = el['countLine']
            text = el['text']
            f.write(f'{name}\n{countLine}\n{text}\n')

def convert_file_text_to_dict(text):
    firstSplit = text.split('\n\n')
    secondSplit = []
    for el in firstSplit:
        secondSplit.append(el.split('\n'))
    result = {}

    for el in secondSplit:
        arr = []
        for index in range(2, len(el)):
            temp = el[index].split(' | ')
            arr.append({'ingredient_name': temp[0], 'quantity': temp[1], 'measure': temp[2]})
        result[el[0]] = arr

    return result

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for el in dishes:
        if el in cook_book:
            ingredients = cook_book[el]
            for ingredient in ingredients:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': str(int(result[ingredient['ingredient_name']]['quantity'])+int(ingredient['quantity'])*person_count)}
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': str(int(ingredient['quantity'])*person_count)}

    return result

cook_book = convert_file_text_to_dict(fileText)
print(cook_book)

ingredients = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)
print(ingredients)

file_name = ['1.txt', '3.txt', '2.txt']
task_three(file_name)

