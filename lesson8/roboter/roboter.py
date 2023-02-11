import string


class Roboter(object):
    """レストランをおすすめするロボット"""

    ask_name_template = string.Template("""\
================================================
こんにちは！私は $name です。あなたの名前は何ですか？
Hello, I am $name What is your name.
================================================
""")

    ask_like_restaurant_template = string.Template("""\
================================================
$user_name さん。どこのレストランが好きですか？
$user_name, which restaurants do you like?
================================================
""")

    final_words_template = string.Template("""\
================================================
$name: $user_name さん。ありがとうございました。
$name: Thank you so much, $user_name!

良い一日を！さようなら。
Have a good day!
================================================  
""")

    recommend_template = string.Template("""\
================================================
私のおすすめのレストランは、$restaurant です。
i recommend $restaurant restaurant.

このレストランは好きですか？ [Yes/No]
Do you like it? [y/n]
================================================  
""")

    def __init__(self, name: str):
        self.__name: str = name
        self.__user_name: str = None
        self.__restaurant: str = None

    @property
    def restaurant(self) -> str:
        return self.__restaurant

    def ask_name(self):
        """ユーザーの名前を質問する"""
        contents: str = self.ask_name_template.substitute(name=self.__name)
        self.__user_name = input(contents)

    def ask_like_restaurant(self):
        """ユーザーの好きなレストランを質問する"""
        contents: str = self.ask_like_restaurant_template.substitute(user_name=self.__user_name)
        self.__restaurant = input(contents).title()
        self.print_final_words()

    def print_final_words(self):
        """ユーザーに最後の言葉を表示する"""
        contents: str = self.final_words_template.substitute(name=self.__name, user_name=self.__user_name)
        print(contents)

    def recommend(self, restaurants: list[str]):
        """おすすめを表示する

        :param restaurants: おすすめに表示するレストランのリスト
        """
        for restaurant in restaurants:
            contents: str = self.recommend_template.substitute(restaurant=restaurant)
            answer: str = input(contents).lower()

            # レストランが好きと返ってきたらおすすめの表示を終了
            if answer in ('yes', 'y'):
                break






