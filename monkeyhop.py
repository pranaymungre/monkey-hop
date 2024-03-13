positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']

print("[0,1,2,3,4,5,6]")
print(positions)

while True:
  move = input("Press 'q' to quit. Enter position of piece: ")

  if move.lower() == 'q':
    print("You Lose")
    break

  move = int(move)

  if move < 0 or move > 6:
   print("Invalid move")
   continue

  if positions[move] == '-':
   print("Invalid Move")
   continue

  empty_index=0

  if positions[move] == 'G':
     if move+1 <=6 and positions[move +1] == '-':
       empty_index = move + 1

     elif move + 2 <=6 and positions[move +2] == '-':
       empty_index = move + 2

     else:
      print("Invalid Move")
      continue

  elif positions[move] == 'B':
        if move - 1 >= 0 and positions[move - 1] == '-':
            empty_index = move - 1

        elif move - 2 >= 0 and positions[move - 2] == '-' and positions[move - 1] == 'G':
            empty_index = move - 2

        else:
            print("Invalid Move")
            continue

  positions[move], positions[empty_index] = positions[empty_index], positions[move]

  print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
  print(positions)

  if positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
      print("You Win!")
      break


