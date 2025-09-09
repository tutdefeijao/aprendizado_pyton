#casamento
names = ['Synara', 'Diogo', 'Doriene', 'Gérson', 'Samuel', 'Késia']

print(f'Olá querido(a) {names[0].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[1].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[2].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[3].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[4].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[5].title()}, espero ver-te em meu casamento')
#certos nomes não poderiam participar
print(f'\nOs respectivos convidados não poderão participar: ')
print(names[4])
print(names[2])

del names[4]
del names[2]
#então inseri outros dois
names.insert(4, 'Jão')
names.insert(2, 'Julha')

print('\n'f'Olá querido(a) {names[0].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[1].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[2].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[3].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[4].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[5].title()}, espero ver-te em meu casamento')

print('\nTemos mais dinheiro, vamos chamar mais pessoas')

names.append('Ellen')
names.append('Tom')
#Inseri novos nomes
print('\n'f'Olá querido(a) {names[0].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[1].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[2].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[3].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[4].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[5].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[6].title()}, espero ver-te em meu casamento')
print(f'Olá querido(a) {names[7].title()}, espero ver-te em meu casamento')

print('\n Infelizmente só 4 pessoas poderão participar')
#agora avisei que não poderiam participar
names_deleted1 = names.pop()
print(f'Olá, {names_deleted1.title()} infelizmente você não irá')
names_deleted2 = names.pop()
print(f'Olá, {names_deleted2.title()} infelizmente você não irá')
names_deleted3 = names.pop()
print(f'Olá, {names_deleted3.title()} infelizmente você não irá')
names_deleted4 = names.pop()
print(f'Olá, {names_deleted4.title()} infelizmente você não irá')

print(len(names))
#Fim do programa
