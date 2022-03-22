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
  puzzle_guess = input(puzzle)
  if puzzle_guess == puzzle_solution:
    print(f"Correct. Key {key_number} collected.")
    backpack.append(f"Key {key_number}")
  else:
    lives -= 1
    print(f"Incorrect. You have {lives} lives remaining.")

  return lives

if __name__ == '__main__':
  main()