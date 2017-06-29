import reports


def print_the_answers(file_name):
    print(reports.get_most_played(file_name))
    print(reports.sum_sold(file_name))
    print(reports.get_selling_avg(file_name))
    print(reports.count_longest_title(file_name))
    print(reports.get_date_avg(file_name))


print_the_answers("game_stat.txt")
