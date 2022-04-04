from threading import Timer

def main():
    
    print("Welcome to the Game")

    player_name = input("what is your name? ")

    print(f"Hello {player_name}.")

    lives = 3
    print(f"You have {lives} remaining lives.")

    backpack = [] # initialise empty list for backpack

    while True:
      direction = input("Which direction do you want to go? Please choose from North, South, East or West.")    

      if direction == "North":
        room_direction = "North"
        puzzle = "What is 2 + 2? "
        puzzle_solution = "4"
        key_number = "1"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

      elif direction == "South":
        room_direction = "South"
        puzzle = "What is 2 + 3? "
        puzzle_solution = "5"
        key_number = "2"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

      elif direction == "East":
        room_direction = "East"
        puzzle = "What is 2 + 4? "
        puzzle_solution = "6"
        key_number = "3"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
      
      elif direction == "West": 
        room_direction = "West"
        puzzle = "What is 2 + 5? "
        puzzle_solution = "7"
        key_number = "4"
        lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

      else:
        print("Room not recognised!")   

      #if back pack is full, open door and win game.
      if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("Key 4" in backpack):
        print("Win!") 
        exit()

      if lives == 0:
        print("Lose!")
        exit()

def in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number):
  print(f"You entered the {room_direction} Room.")  
  
  # Implement input timer
  time_limit = 3
  timeout_container = [False]
  lives_container = [lives]
  t = Timer(time_limit, check_time_out, args=(lives_container,timeout_container,))
  t.start()
  print(f"You have {time_limit} seconds to choose the correct answer...\n")
  puzzle_guess = input(puzzle)
  t.cancel()
  lives = lives_container[0]
  timeout = timeout_container[0]

  if not timeout:
    if puzzle_guess == puzzle_solution:
      if f"Key {key_number}" not in backpack:
        print(f"Correct. Key {key_number} collected.")
        backpack.append(f"Key {key_number}")
      else:
        print("You have already collected this key!")
    else:
      lives -= 1
      print(f"Incorrect. You have {lives} lives remaining.")

  return lives

def check_time_out(lives_container,timeout_container):
  lives_container[0] -= 1
  print(f"Time out! You have {lives_container[0]} lives remaining. Press Enter to continue.")
  timeout_container[0] = True
  return lives_container, timeout_container

if __name__ == '__main__':
  main()