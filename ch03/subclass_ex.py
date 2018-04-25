class DistinctError(ValueError):
    """distinctdictに重複した値を追加した時に上がる例外"""


class distinctdict(dict):
    """重複した値が登録できない辞書"""
    def __setitem__(self, key, value):
        if value in self.values():
            if (
                    (key in self and self[key] != value) or
                    key not in self
            ):
                raise DistinctError(
                    "この値はすでに別のキーで登録されています"
                )

        super().__setitem__(key, value)


class Folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self, nesting=0):
        offset = "  " * nesting
        print('%s%s/' % (offset, self.name))

        for element in self:
            if hasattr(element, 'dir'):
                element.dir(nesting + 1)
            else:
                print('%s  %s' % (offset, element))
