import reports


def print_the_answers(file_name, year, genre, title):
    print(reports.count_games(file_name))
    print(reports.decide(file_name, year))
    print(reports.get_latest(file_name))
    print(reports.count_by_genre(file_name, genre))
    print(reports.get_line_number_by_title(file_name, title))
    print(reports.sort_abc(file_name))
    print(reports.get_genres(file_name))
    print(reports.when_was_top_sold_fps(file_name))


print_the_answers("game_stat.txt", "2000", "First-person shooter", "Crysis")
