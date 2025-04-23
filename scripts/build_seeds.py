# save as build_nigeria_seeds.py
import json, pathlib, urllib.request, textwrap, datetime

URL = ("https://raw.githubusercontent.com/afeibukun/"
       "nigerian-state-lgas-wards-polling-units/"
       "main/states-and-lgas-and-wards.json")
data = json.loads(urllib.request.urlopen(URL).read().decode())

state_rows, lga_rows, ward_rows = [], [], []
state_id = lga_id = 0

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for state in data:
    state_id += 1
    state_name = state["state"].title()
    state_rows.append(f"({state_id},'{state_name}','enabled','{timestamp}','{timestamp}')")

    for lga in state["lgas"]:
        lga_id += 1
        lga_name = lga["lga"].replace('-', ' ').title()
        lga_rows.append(f"({lga_id},{state_id},'{lga_name}','enabled','{timestamp}','{timestamp}')")

        for ward in lga["wards"]:
            ward_name = ward.replace("'", "''").replace('-', ' ').title()
            ward_rows.append(f"({lga_id},'{ward_name}','enabled','{timestamp}','{timestamp}')")

def write(name, cols, rows):
    pathlib.Path(name).write_text(
        "INSERT INTO `{}` ({}) VALUES\n".format(name.split('_')[1],
            ",".join("`{}`".format(c) for c in cols)) +
        ",\n".join(rows) + ";\n", "utf-8")

write("nigeria_states_seed.sql",
      ("id","name","status","created_at","updated_at"), state_rows)
write("nigeria_lgas_seed.sql",
      ("id","state_id","name","status","created_at","updated_at"), lga_rows)
write("nigeria_wards_seed.sql",
      ("lga_id","name","status","created_at","updated_at"), ward_rows)

print("✓  wrote all three seed files")
