def check_query(query):
    tokens = query.split(',')
    return(tokens[1].strip())
# напишите код тела функции


# дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]



for q in queries:
    result = check_query(q)
    print(q, '-', result)

