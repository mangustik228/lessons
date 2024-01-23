import pandas as pd

from sqlalchemy import text, create_engine

from app.config import db


q = "SELECT * FROM product"

engine = create_engine(db.url)

with engine.connect() as connection:
    df = pd.read_sql_query(text(q), connection)

print(df.to_string(index=False), end='\n\n')
print(f'Итого значений в бд: {len(df)}')
