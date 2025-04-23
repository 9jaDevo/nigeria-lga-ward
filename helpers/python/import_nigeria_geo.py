import pathlib
import sqlalchemy as sa

engine = sa.create_engine("mysql+pymysql://root:YOURPASS@localhost/armsserv")

with engine.begin() as conn:
    for fname in ["nigeria_states_seed.sql", "nigeria_lgas_seed.sql", "nigeria_wards_seed.sql"]:
        sql = pathlib.Path("../data", fname).read_text()
        conn.exec_driver_sql(sql)

print("✔ import finished")
