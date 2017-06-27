from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, sort_abc, get_genres


def export_to_txt(file_name, year, genre, title, exp_file="exported_answers.txt"):
    with open(exp_file, "w") as text_file:
        text_file.write(str(count_games(file_name)))
        text_file.write("\n")
        text_file.write(str(decide(file_name, year)))
        text_file.write("\n")
        text_file.write(str(get_latest(file_name)))
        text_file.write("\n")
        text_file.write(str(count_by_genre(file_name, genre)))
        text_file.write("\n")
        text_file.write(str(get_line_number_by_title(file_name, title)))
        text_file.write("\n")
        text_file.write(str(sort_abc(file_name)))
        text_file.write("\n")
        text_file.write(str(get_genres(file_name)))


export_to_txt("game_stat.txt", "2000", "RPG", "Minecraft", exp_file="exported_answers.txt")
