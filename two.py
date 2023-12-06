def main():
    with open("C:\\Users\\Visie Groep\\PycharmProjects\\AdventCode\\Advent inputs\\input2.txt", "r") as file:
        lines = file.readlines()
        games = []
        legal_games = 0
        for line in lines:
            games.append(line.split(":")[1].lstrip().rstrip("\n").split(";"))
        for game, game_line in enumerate(games, 1):
            legal = True
            for pull, pull_line in enumerate(game_line):
                for color_line in pull_line.split(","):
                    if "red" in color_line:
                        if int(color_line.split()[0]) > 12:
                            legal = False
                    elif "green" in color_line:
                        if int(color_line.split()[0]) > 13:
                            legal = False
                    else:
                        if int(color_line.split()[0]) > 14:
                            legal = False
            if legal:
                legal_games += game

    return legal_games


def main2():
    with open("C:\\Users\\Visie Groep\\PycharmProjects\\AdventCode\\Advent inputs\\input2.txt", "r") as file:
        lines = file.readlines()
        games = []
        sum_of_powers = 0
        min_reds = []
        for line in lines:
            games.append(line.split(":")[1].lstrip().rstrip("\n").split(";"))
        for game, game_line in enumerate(games, 1):
            min_red, min_green, min_blue = 0, 0, 0
            for pull, pull_line in enumerate(game_line):
                for color_line in pull_line.split(","):
                    if "red" in color_line:
                        min_red = max(int(color_line.split()[0]), min_red)
                    elif "green" in color_line:
                        min_green = max(int(color_line.split()[0]), min_green)
                    else:
                        min_blue = max(int(color_line.split()[0]), min_blue)
            min_reds.append(min_red)
            sum_of_powers += min_red * min_green * min_blue

    return sum_of_powers, min_reds


if __name__ == '__main__':
    ans, _ = main2()
    print(ans)
