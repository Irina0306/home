team1_num=5
team2_num=6
score_1=40
score_2=42
team1_time= 1552.512
team2_time= 2153.31451
task_total= 82
time_avg= 45.2
if score_1 > score_2 or score_1== score_2 and team1_time> team2_time:
    result= "Победа мастера кода!"
elif score_1< score_2 or score_1== score_2 and team1_time< team2_time:
    result= 'Победа команды Волшебники данных'
else:
    result= 'Ничья!'


print('В команде Мастера кода участников:%s' % 5)
print('Итого сегодня в командах участников: %s и %s' %(5, 6))
print('Команда Волшебники данных решила задач:{score_2}'.format(score_2=42))
print('Волшебники данных решили задачи за {} c'.format(18015.2))
print(f'команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: победа команды {result} !')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу')