user = {'Камин комплект Старый Замок':
{'count': 1, 'price': 28490}, 
'Полусапоги Betsy':{'count': 2, 'price': 2399}, 
'Семь навыков высокоэффективных людей':{'count': 1, 'price': 437}}
summa = user['Камин комплект Старый Замок']['count']*user['Камин комплект Старый Замок']['price']
summa += user['Полусапоги Betsy']['count']*user['Полусапоги Betsy']['price']
summa += user['Семь навыков высокоэффективных людей']['count']*user['Семь навыков высокоэффективных людей']['price']
print(summa)
