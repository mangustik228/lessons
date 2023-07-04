from jinja2 import Template
from loguru import logger


name = "Fedor"


def main():
    tm = Template("Привет {{ name }}")
    msg = tm.render(name=name)
    logger.info(msg)


if __name__ == '__main__':
    main()
