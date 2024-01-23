from datetime import datetime
import enum
from typing import Annotated
from sqlalchemy import DateTime, ForeignKey, String, func, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker


engine = create_engine("sqlite:///example.sqlite", echo=True)
session_maker = sessionmaker(engine)

id_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime, mapped_column(server_default="TIMEZONE('utc',now())")]
updated_at = Annotated[
    datetime, mapped_column(default=datetime.utcnow)]
str_200 = Annotated[str, 200]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_200: String(200),
    }


class Worker(Base):
    __tablename__ = "worker"
    id: Mapped[id_pk]
    name: Mapped[str]

    def __str__(self):
        return f"worker [{self.name}]"


class Workload(enum.Enum):
    parttime = "partime"
    fulltime = "fulltime"


class Resume(Base):
    __tablename__ = "resume"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    title: Mapped[str_200]
    salary: Mapped[int | None]
    workload: Mapped[Workload]  # можно сослаться на enum
    worker_id: Mapped[int] = mapped_column(
        ForeignKey("worker.id", ondelete="CASCADE"))  # возможно удалить также по схеме: SET NULL
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
