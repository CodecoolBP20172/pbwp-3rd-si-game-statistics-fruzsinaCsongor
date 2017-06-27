
from collections import OrderedDict

stats = {}
with open("game_stat.txt") as inputfile:
    for line in inputfile:
        title, copies, release, gen, publ = (
            item.strip() for item in line.split('\t', 4))
        stats[title] = dict(zip(("title", "copies", "release", "genre", "publisher"),
                            (title, copies, release, gen, publ)))


def count_games(file_name):
    with open(file_name) as inputfile:
        return sum(1 for _ in inputfile)


def decide(file_name, year):
    with open(file_name) as inputfile:
        return any(str(year) in line for line in inputfile)


def get_latest(file_name):
    release_dict = {}
    for game in stats.values():
        release_dict[game["title"]] = game["release"]
    release_dict = OrderedDict(sorted(release_dict.items(), key=lambda t: t[1]))
    return list(release_dict.items())[-1][0]


def count_by_genre(file_name, genre):
    genre_list = []
    for game in stats:
        for value in stats[game].values():
            if value == genre:
                genre_list.append(game)
    return len(genre_list)


def get_line_number_by_title(file_name, title):
    title_list = ["0"]
    with open(file_name, "r") as inputfile:
        for line in inputfile:
            title_list.append(line.split("\t", 1)[0])
    for item in title_list:
        if item == title:
            return title_list.index(title)


def sort_abc(file_name):
    abc_list = []
    for game in sorted(stats.keys(), key=str.lower):
        abc_list.append(game)
    return abc_list


def get_genres(file_name):
    genres = set()
    for game in stats.values():
        genres.add(game["genre"])
    return sorted(list(genres), key=str.lower)


# def when_was_top_sold_fps(file_name):
#
