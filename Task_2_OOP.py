cook_book = {}
with open('recipes.txt', encoding='utf-8') as recipes:
    for line in recipes:
        dish_name = line.strip()
        if not dish_name:
            continue
        else:
            ingredients_count = int(recipes.readline().strip())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredients_data = recipes.readline().strip().split(' | ')
                ingredients_dict = {}
                ingredients_dict['ingredient_name'] = ingredients_data[0]
                ingredients_dict['quantity'] = int(ingredients_data[1])
                ingredients_dict['measure'] = ingredients_data[2]
                ingredients_list.append(ingredients_dict)
            cook_book[dish_name] = ingredients_list


def get_shop_list_by_dishes(dishes, person_count):
    shop_list ={}
    for dish in dishes:
        if dish not in cook_book.keys():
            print('Такого блюда нет в книге рецептов')
            continue
        else:
            ingredients_lst = cook_book[dish]
            for ingredient in ingredients_lst:
                ingredient_name = ingredient['ingredient_name']
                count = ingredient['quantity']
                meas = ingredient['measure']
                all_count = count * person_count
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] ={'measure': meas, 'quantity': all_count}
                else:
                    shop_list[ingredient_name]['quantity'] += all_count
    return shop_list
print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))