from loguru import logger
from sqlalchemy import select
import app.models as M
from sqlalchemy.orm.attributes import instance_dict


def with_db(func: callable):
    def inner(*args, **kwargs):
        M.engine.echo = True
        M.Base.metadata.create_all(M.engine)
        logger.debug("db created")
        func(*args, **kwargs)
        M.Base.metadata.drop_all(M.engine)
        logger.debug("db droped")
    return inner


@with_db
def main():
    logger.debug("hello world")

    with M.session_maker() as session:
        worker = M.Worker(name="jopa")
        session.add(worker)
        session.commit()

    with M.session_maker() as session:
        stmt = select(M.Worker)
        result = session.execute(stmt)
        logger.success(f"{result.mappings().first()['Worker']!r}")

    logger.debug("success")


if __name__ == '__main__':
    main()
