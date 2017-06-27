from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, sort_abc, get_genres


def print_the_answers(file_name, year, genre, title):
    print(count_games(file_name), "\n")
    print(decide(file_name, year), "\n")
    print(get_latest(file_name), "\n")
    print(count_by_genre(file_name, genre), "\n")
    print(get_line_number_by_title(file_name, title), "\n")
    print(sort_abc(file_name), "\n")
    print(get_genres(file_name), "\n")


print_the_answers("game_stat.txt", "2000", "First-person shooter", "Crysis")
