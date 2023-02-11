import csv
import os

csv_filename = 'ranking.csv'
filed1 = 'NAME'
filed2 = 'COUNT'
fieldnames = [filed1, filed2]


def exists() -> bool:
    """csvが存在するかどうかの判定をする

    :return: csvが存在すれば True / 存在しなければ False
    """
    return os.path.exists(csv_filename)


def read() -> list[dict]:
    """csvがあれば内容を返す

    :return: csvの内容
    """
    if exists():
        with open(csv_filename, 'r') as file:
            reader = list(csv.DictReader(file))
            return reader
    else:
        return []


def write(inputs: list[dict]):
    """csvに書き込む

    :param inputs: csvに書き込む内容
    """
    with open(csv_filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames)

        # ヘッダー行を書き込む
        writer.writeheader()

        # データ行を書き込む
        for i in inputs:
            writer.writerow(i)


def write_increments(restaurants: str):
    """csvを読み込んで指定されたレストランが存在すればCOUNTをインクリメント。
    存在しなければ、新規に追加する。

    :param restaurants: 指定されたレストラン
    """
    # csvの内容を取得
    csv_list: list[dict] = read()

    # csvがあった場合
    if csv_list:
        for row in csv_list:
            # csvに指定されたレストランがあった場合
            if row[filed1] == restaurants:
                row[filed2] = str(int(row[filed2]) + 1)
                break
        # csvに指定されたレストランがなかった場合
        else:
            csv_list.append({filed1: restaurants, filed2: '1'})

        # csvに書き込み
        write(csv_list)

    # csvがなかった場合
    else:
        # csvに新規で書き込み
        write([{filed1: restaurants, filed2: '1'}])


def get_recommend_restaurants() -> list[str]:
    """csvがあればおすすめのレストランをリストアップする

    :return: レストランをリストアップ舌リスト
    """
    # csvの内容を取得
    csv_list: list[dict] = read()

    # csvがあった場合
    if csv_list:
        sort_csv_list = sorted(csv_list, key=lambda x: int(x[filed2]), reverse=True)
        return list(map(lambda x: x[filed1], sort_csv_list))
    # csvがなかった場合
    else:
        return []


