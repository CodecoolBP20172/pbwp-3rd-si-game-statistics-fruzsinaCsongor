import reports


def print_the_answers(file_name, title):
    print(reports.get_most_played(file_name))
    print(reports.sum_sold(file_name))
    print(reports.get_selling_avg(file_name))
    print(reports.count_longest_title(file_name))
    print(reports.get_date_avg(file_name))
    print(reports.get_game(file_name, title))
    print(reports.count_grouped_by_genre(file_name))
    print(reports.get_date_ordered(file_name))


print_the_answers("game_stat.txt", "Counter-Strike")
