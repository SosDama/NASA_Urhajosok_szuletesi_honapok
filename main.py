import pandas as pd


def open_csv():
    csv_file = pd.read_csv("astronauts.csv", skipinitialspace=True, usecols=["Birth Date"])
    return csv_file.values.tolist()


def counting(months):
    month_list = [int(x[:x.find("/")]) for i in months for x in i]
    total = len(month_list)
    degree_dict = {}
    for month in range(1, 13):
        degree_dict[str(month)] = [month_list.count(month), round(month_list.count(month) / total * 100, 1)]
    return degree_dict


def find_most_commonests(d):
    common_months = []
    while len(common_months) < 3:
        max_val = [0, 0]
        max_key = ""
        for key, val in d.items():
            if val[0] > max_val[0]:
                max_val = val
                max_key = key
        common_months.append((max_key, str(max_val[1])))
        del d[max_key]
    return common_months


def main():
    print("A program NASA űrhajósok 3 leggyakoribb születési hónapját mondja meg.")
    months = open_csv()
    d = counting(months)
    answers = find_most_commonests(d)
    for i, ans in enumerate(answers):
        print(f"{i+1}. leggyakoribb születési hónap: {ans[0]}, {ans[1]}%-os aránnyal.")


main()
