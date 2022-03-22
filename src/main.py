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
        print(f"You entered the North Room.")
        puzzle_guess = input("What is 2 + 2? ")
        if puzzle_guess == "4":
          print(f"Correct. Key 1 collected.")
          backpack.append(f"Key 1")
        else:
          lives -= 1
          print(f"Incorrect. You have {lives} lives remaining.")

      elif direction == "South":
        print(f"You entered the South Room.")
        puzzle_guess = input("What is 2 + 3? ")
        if puzzle_guess == "5":
          print(f"Correct. Key 2 collected.")
          backpack.append(f"Key 2")
        else:
          lives -= 1
          print(f"Incorrect. You have {lives} lives remaining.")

      elif direction == "East":
        print(f"You entered the East Room.")
        puzzle_guess = input("What is 2 + 4? ")
        if puzzle_guess == "6":
          print(f"Correct. Key 3 collected.")
          backpack.append(f"Key 3")
        else:
          lives -= 1
          print(f"Incorrect. You have {lives} lives remaining.")

      elif direction == "West": 
        print(f"You entered the West Room.")
        puzzle_guess = input("What is 2 + 5? ")
        if puzzle_guess == "7":
          print(f"Correct. Key 4 collected.")
          backpack.append(f"Key 4")
        else:
          lives -= 1
          print(f"Incorrect. You have {lives} lives remaining.")

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