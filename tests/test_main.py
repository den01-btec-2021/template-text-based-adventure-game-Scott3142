import pytest, src.main

def test_in_room():
    
    ## Test correct input inside room ##
    input_value_correct = ["14"] # this is the user's (correct) guess
    output_correct = []

    backpack = []
    lives = 3
    room_direction = "North"
    puzzle = "What is 6 + 8?"
    puzzle_solution = "14"
    key_number = "1"

    def mock_input_correct(s):
      output_correct.append(s)
      return input_value_correct[0]

    src.main.input = mock_input_correct
    src.main.print = lambda s : output_correct.append(s)

    src.main.in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

    assert output_correct == [f"You entered the {room_direction} Room.",puzzle,f"Correct. Key {key_number} collected."]

    ## Test incorrect input inside room #
    input_value_incorrect = ["15"] # this is the user's (incorrect) guess
    output_incorrect = []

    def mock_input_incorrect(s):
      output_incorrect.append(s)
      return input_value_incorrect[0]

    src.main.input = mock_input_incorrect
    src.main.print = lambda s : output_incorrect.append(s)

    src.main.in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
    assert output_incorrect == [f"You entered the {room_direction} Room.",puzzle,f"Incorrect. You have {lives-1} lives remaining."]

    ## Test second correct input inside room - checks for response that Key 1 has already been collected ##
    input_value_correct = ["14"] # this is the user's (correct) guess
    output_correct_run_two = []

    def mock_input_correct(s):
        output_correct_run_two.append(s)
        return input_value_correct[0]

    src.main.input = mock_input_correct
    src.main.print = lambda s : output_correct_run_two.append(s)

    src.main.in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)

    assert output_correct_run_two == [f"You entered the {room_direction} Room.",puzzle,f"You have already collected this key!"]