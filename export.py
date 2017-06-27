from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, sort_abc, get_genres


def export_to_txt(file_name, year, genre, title, exp_file="answers.txt"):
    with open(exp_file, "w") as text_file:
        text_file.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(str(count_games(file_name)),
                                                              str(decide(file_name, year)),
                                                              str(get_latest(file_name)),
                                                              str(count_by_genre(file_name, genre)),
                                                              str(get_line_number_by_title(file_name, title)),
                                                              str(sort_abc(file_name)),
                                                              str(get_genres(file_name))))


export_to_txt("game_stat.txt", "2000", "RPG", "Minecraft", exp_file="answers.txt")
