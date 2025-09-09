#Recriar o casamento porém com os conhecimentos que tenho agora
names = ['synara', 'diogo', 'gerson', 'dorinha', 'lucia', 
'isaac', 'joão', 'julha', 'emilly', 'gabriel', 'samuel', 'késia', 'otávio', 'giovanna']
for name in names:
    print(f'Olá querido(a) {name.title()}, espero te ver no meu casamento!')

print('\nInfelizmente os seguintes nomes não poderão participar: ')
print(names[13])
print(names[12])

namedeleted1 = names.pop(12)
namedeleted2 = names.pop(12)

#inserir outros dois nomes
names.insert(12, 'tom builder')
names.insert(13,'ellen')

print('\nEsses serão os nomes que farão parte do nosso casamento: ')
for name in names: 
   print(name.title())

#inserir mais nomes
names.append('otávio')
names.append('giovanna')
