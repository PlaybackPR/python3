#friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск', 'Вася': 'Париж', 'Толя': 'Томск'}
#print("Вот в каких городах живут мои друзья: " + ', '.join(friends.values()))

#friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск', 'Вася': 'Париж', 'Толя': 'Томск'}

#for friend in friends:
 #   print(friend + ' живет в городе ' + friends[friend])

#favorite_songs = {
   # 'Серёга': ["Unforgiven", "Holiday", "Highway to hell"],
   # 'Соня': ["Shake it out", "Don't stop me now", "Наше лето"],
   # 'Дима': ["Владимирский централ", "Мурка", "Третье сентября"]
#}

# напишите код, который напечатает на экран, сколько у Димы любимых песен
#print(len(favorite_songs['Дима']))
# здесь напишите код, который напечатает
#print(', '.join(favorite_songs['Соня']))
# все любимые песни Сони через запятую и пробел ', '

friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]
print('Лена живёт в городе ' + friends['Лена'])