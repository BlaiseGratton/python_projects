import random

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
         (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
         (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

def get_locations():
  monster = random.choice(CELLS)
  door = random.choice(CELLS)
  start = random.choice(CELLS)
  
  if monster == door or monster == start or door == start:
    return get_location()
  
  return monster, door, start

def move_player(player, move):
  # player = (x, y)
  x, y = player
  
  if move == 'LEFT':
    y -= 1
  elif move == 'RIGHT':
    y += 1
  elif move == 'UP':
    x -= 1
  elif move == 'DOWN':
    x += 1
    
  return x, y

def get_moves(player):
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # player = (x, y)
  
  if player[1] == 0:
    moves.remove('LEFT')
  if player[1] == 6:
    moves.remove('RIGHT')
  if player[0] == 0:
    moves.remove('UP')
  if player[0] == 6:
    moves.remove('DOWN')
  
  return moves

def draw_map(player):
  print(' _ _ _ _ _ _ _ ')
  tile = '|{}'
  
  for idx, cell in enumerate(CELLS):
    if idx in [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54]:
      if cell == player:
        print(tile.format('X'),)# end='')  python 3.x thing?
      else:
        print(tile.format('_'),)# end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))
  
monster, door, player = get_locations()

print("Welcome to the dungeon!")

while True:
  moves = get_moves(player)
  
  print("You're currently in room {}".format(player))
  
  draw_map(player)
  
  print("You can move {}".format(moves))
  print("Enter QUIT to quit")
  
  move = input("> ")
  move = move.upper()
  
  if move == 'QUIT':
    break
    
  if move in moves:
    player = move_player(player, move)
  else: 
    print("** Walls are hard, stop walking into them! **")
    continue
  
  if player == door:
    print("You escaped!")
    break
  elif player == monster:
    print("You were eaten by the grue!")
    break
