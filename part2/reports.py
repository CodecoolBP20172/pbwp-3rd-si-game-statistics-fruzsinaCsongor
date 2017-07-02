from statistics import mean
from math import ceil
from collections import OrderedDict

stats = {}
with open("game_stat.txt") as inputfile:
    for line in inputfile:
        title, copies, release, gen, publ = (
            item.strip() for item in line.split('\t', 4))
        stats[title] = dict(zip(("title", "copies", "release", "genre", "publisher"),
                            (title, copies, release, gen, publ)))


def get_most_played(file_name):
    copies_dict = {}
    for val1 in stats.values():
        for val2 in val1.values():
            copies_dict[val1["title"]] = float(val1["copies"])
    copies_dict = OrderedDict(sorted(copies_dict.items(), key=lambda t: t[1]))
    return list(copies_dict.items())[-1][0]


def sum_sold(file_name):
    copies_list = [float(val2) for val1 in stats.values()
                   for key2, val2 in val1.items()
                   if key2 == "copies"]
    return round(sum(copies_list), 2)


def get_selling_avg(file_name):
    copies_list = [float(val2) for val1 in stats.values()
                   for key2, val2 in val1.items()
                   if key2 == "copies"]
    return mean(copies_list)


def count_longest_title(file_name):
    names_list = [game for game in stats.keys()]
    longest = sorted(names_list, key=len)[-1]
    return len(longest)


def get_date_avg(file_name):
    date_list = [int(val2) for val1 in stats.values()
                 for key2, val2 in val1.items()
                 if key2 == "release"]
    return ceil(mean(date_list))


def get_game(file_name, title):
    with open("game_stat.txt", "r") as inputfile:
        for line in inputfile:
            if line.split("\t", 1)[0] == title:
                game = line
    game_list = [x.strip() for x in game.split("\t")]
    game_list[1] = float(game_list[1])
    game_list[2] = int(game_list[2])
    return game_list


def count_grouped_by_genre(file_name):
    genre_list = [val2 for val in stats.values()
                  for key2, val2 in val.items()
                  if key2 == "genre"]
    return {x: genre_list.count(x) for x in genre_list}


def get_date_ordered(file_name):
    date_dict = {}
    for val1 in stats.values():
        for val2 in val1.values():
            date_dict[val1["title"]] = int(val1["release"])
    date_dict = list(v[0] for v in sorted(date_dict.items(),
                     key=lambda kv: (-kv[1], kv[0])))
    return date_dict
