from roboter import csv_utils
from roboter.roboter import Roboter


def main():
    roboter = Roboter('Roboko')

    # 名前を尋ねる
    roboter.ask_name()

    if csv_utils.exists():
        # csvからCOUNTが多い順にレストランの名前を入れたリストを取得
        csv_recommend_list = csv_utils.get_recommend_restaurants()

        # おすすめを表示する
        roboter.recommend(csv_recommend_list)

    # 好きなレストランを尋ねる
    roboter.ask_like_restaurant()

    # csvにレストランを書き込む
    csv_utils.write_increments(roboter.restaurant)


if __name__ == '__main__':
    main()
