import reports


def export_to_txt(file_name, year, genre, title, exp_file="answers.txt"):
    with open(exp_file, "w") as text_file:
        text_file.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            str(reports.count_games(file_name)),
            str(reports.decide(file_name, year)),
            str(reports.get_latest(file_name)),
            str(reports.count_by_genre(file_name, genre)),
            str(reports.get_line_number_by_title(file_name, title)),
            str(reports.sort_abc(file_name)),
            str(reports.get_genres(file_name)),
            str(reports.when_was_top_sold_fps(file_name))))


export_to_txt("game_stat.txt", "2000", "First-person shooter", "Crysis", exp_file="answers.txt")
