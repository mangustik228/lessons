import re
from loguru import logger

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050
BOOK : dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    edit_text = re.sub(r'[.,!?:;]\.+$', '', text[start:start+size])
    edit_text = re.findall(r'(?s).+[.,!?:;]', edit_text)
    edit_text = re.sub(r'\n(?!    )', '0', edit_text[0])  # убирает лишние \n
    return edit_text, len(edit_text)


@logger.catch
def _prepare_book(path: str) -> dict: 
    with open(path, 'r') as fp:
        book_txt = fp.read()
    i = start = len_txt = 0
    while True:
        if start >= len(book_txt):
            break
        txt, len_txt = _get_part_text(book_txt, start, PAGE_SIZE)
        start += len_txt
        BOOK[i+1] = txt.strip()
        i += 1

_prepare_book(BOOK_PATH)