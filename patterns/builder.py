

class HtmlBuilder:
    def __init__(self, root_tag: str):
        self.root_tag = root_tag
        self._root = HtmlElement(root_tag)

    def add_child(self, child_tag, child_text):
        self._root.elements.append(HtmlElement(child_tag, child_text))

    def __str__(self):
        return str(self._root)


class HtmlElement:
    def __init__(self, tag: str = '', text: str = ''):
        self.tag = tag
        self.text = text
        self.elements: list[HtmlElement] = []

    def _str(self):
        lines = []
        lines.append(f'<{self.tag}>')

        if self.text:
            lines.append(f'{self.text}')

        for e in self.elements:
            lines.append(e._str())

        lines.append(f'</{self.tag}>')

        return ''.join(lines)

    def __str__(self):
        return self._str()

    @staticmethod
    def create(tag):
        return HtmlBuilder(tag)


def main():
    builder = HtmlElement.create('ul')
    builder.add_child('li', "hello")
    builder.add_child("li", "world")
    print(builder)


if __name__ == '__main__':
    main()
