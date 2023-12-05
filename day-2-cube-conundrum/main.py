filename = "puzzle_input.csv"

POSSIBLE_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_games = []
total = 0

with open(filename, 'r') as input_file:
    for game_id, line in enumerate(input_file.readlines(), 1):
        cube_sets = line.strip().split(": ")[1].split("; ")

        possible = True
        for cube_set in cube_sets:
            cubes = cube_set.split(", ")

            for cube in cubes:
                count, color = cube.split(" ")

                if POSSIBLE_CUBES[color] < int(count):
                    possible = False
                    break

        game_result = {
            "id": game_id,
            "result_possible": possible
        }

        if game_result["result_possible"] is True:
            possible_games.append(game_id)

    for game in possible_games:
        total += game
    print(total)
