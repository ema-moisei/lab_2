""". Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a
start position (integer). The function will return the song composed by going though the musical notes beginning with
the start position and following the moves given as parameter.

Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] """


def compose(compose_list):
    musical_notes = [compose_list[0][2]]
    current_index = compose_list[0].index(compose_list[0][2])
    new_list = compose_list[0][current_index:] + compose_list[0][:current_index]
    for move in compose_list[1]:
        musical_notes.append(new_list[move])
        new_list = new_list[move:] + new_list[:move]
    print(musical_notes)


def main():

    compose_list = (["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    compose(compose_list)


if __name__ == "__main__":
    main()
