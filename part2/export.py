import reports


def export_to_txt(file_name, exp_file="answers.txt"):
    with open(exp_file, "w") as text_file:
        text_file.write("{}\n{}\n{}\n{}\n{}".format(
            str(reports.get_most_played(file_name)),
            str(reports.sum_sold(file_name)),
            str(reports.get_selling_avg(file_name)),
            str(reports.count_longest_title(file_name)),
            str(reports.get_date_avg(file_name))))


export_to_txt("game_stat.txt", exp_file="answers.txt")
