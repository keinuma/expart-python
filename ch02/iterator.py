class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """
        Return the next element
        :return:
        """
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """
        Return the iterator itself.
        :return:
        """
        return self


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def power(values):
    for value in values:
        print('%s を供給' % value)
        yield value


def adder(values):
    for value in values:
        print('%s に値を追加' % value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


def psychologist():
    print('あなたの悩みを聞かせてください')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print('自分自身に問いかけをしすぎないようにしましょう')
            elif '良い' in answer:
                print('それは良いですね。ぜひやりましょう')
            elif '悪い' in answer:
                print('悲観的にならないようにしましょう')
            else:
                print('ちょっとよくわからないです')
