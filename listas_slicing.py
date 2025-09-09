players = ['neymar', 'fenomeno', 'pele', 'cr7','messi', 'croif', 'maradona', 'danialves', 'honda', 'vampeta', 'dida', 'alisson']
print("there's are the best players of the world: \n")
for player in players[:]:
    print(player.title())

my_player = players[:]

print('\nmy best players are: ')
for my_player in players[0:4]:
  print(my_player.title())

friend_player = players[:]

print(f'\nmy friend favorite players are: ')
for friend_player in players[6:]:
   print(friend_player.title())