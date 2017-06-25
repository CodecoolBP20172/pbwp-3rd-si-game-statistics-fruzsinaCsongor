def count_games(file_name):
    with open(file_name) as inputfile:
        return sum(1 for _ in inputfile)


def decide(file_name, year):
    with open(file_name) as inputfile:
        return any(year in line for line in inputfile)


# def get_latest(file_name):
#


# def count_by_genre(file_name, genre):
#


# def get_line_number_by_title(file_name, title):
#


# def sort_abc(file_name):
#


# def get_genres(file_name):
#


# def when_was_top_sold_fps(file_name):
#
