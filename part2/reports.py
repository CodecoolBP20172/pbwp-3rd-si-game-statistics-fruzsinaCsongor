from statistics import mean

stats = {}
with open("game_stat.txt") as inputfile:
    for line in inputfile:
        title, copies, release, gen, publ = (
            item.strip() for item in line.split('\t', 4))
        stats[title] = dict(zip(("title", "copies", "release", "genre", "publisher"),
                            (title, copies, release, gen, publ)))


# def get_most_played(file_name):


def sum_sold(file_name):
    copies_list = []
    for val1 in stats.values():
        for key2, val2 in val1.items():
            if key2 == "copies":
                copies_list.append(float(val2))
    return round(sum(copies_list), 2)


def get_selling_avg(file_name):
    copies_list = []
    for val1 in stats.values():
        for key2, val2 in val1.items():
            if key2 == "copies":
                copies_list.append(float(val2))
    return mean(copies_list)


# def count_longest_title(file_name):


# def get_date_avg(file_name):


# def get_game(file_name, title):


# def count_grouped_by_genre(file_name):


# def get_date_ordered(file_name):
