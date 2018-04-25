class Mama:
    def says(self):
        print('宿題をしなさい')


class SisterOld(Mama):
    def says(self):
        # 古いやり方
        Mama.says(self)
        print('あと、部屋の掃除もしなさい')


class SisterSuper(Mama):
    def says(self):
        super(SisterSuper, self).says()
        print('あと、部屋の掃除もしなさい')


class SisterNew(Mama):
    def says(self):
        # 引数なしのsuperはメソッド内部のみ利用可能
        super().says()
        print('あと、部屋の掃除もしなさい')


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return "と".join(self.toppings) + "がトッピングされたピザ"

    @classmethod
    def recommend(cls):
        """
        いくつかのトッピングが載ったお勧めのピザの紹介
        :return:
        """
        return cls(['スパム', 'ハム', '卵'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """親クラスと同じようなお勧めピザだが、スパムを大量に追加"""
        recommended = super(VikingPizza).recommend()
        recommended.toppings += ['スパム'] * 5
        return recommended
