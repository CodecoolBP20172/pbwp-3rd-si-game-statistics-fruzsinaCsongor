
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


def sort_abc(file_name):
    stats = {}
    with open(file_name) as inputfile:
        for line in inputfile:
            title, copies, release, genre, publisher = (
                item.strip() for item in line.split('\t', 4))
            stats[title] = dict(zip(("title", "copies", "release", "genre", "publisher"),
                                (title, copies, release, genre, publisher)))
    abc_list = []
    for game in sorted(stats.keys()):
        abc_list.append(game)
    return abc_list


def get_genres(file_name):
    stats = {}
    with open(file_name) as inputfile:
        for line in inputfile:
            title, copies, release, genre, publisher = (
                item.strip() for item in line.split('\t', 4))
            stats[title] = dict(zip(("title", "copies", "release", "genre", "publisher"),
                                (title, copies, release, genre, publisher)))
    genres = set()
    for game in stats.values():
        genres.add(game["genre"])
    return sorted(list(genres))


# def when_was_top_sold_fps(file_name):
#
