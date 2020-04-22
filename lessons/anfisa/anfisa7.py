def print_shopping_list(pizza, salad):# напишите здесь свою функцию
    recipe1 = set(pizza)
    recipe2 = set(salad)
    shopping_list = (recipe1.union(recipe2))
    print(', '.join(shopping_list))


pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print_shopping_list(pizza, salad)