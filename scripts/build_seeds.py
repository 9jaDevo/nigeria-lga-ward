#!/usr/bin/env python3
"""
Builds states, LGAs & wards seed SQL from the open‐source JSON.
Writes:
  • data/nigeria_states_seed.sql
  • data/nigeria_lgas_seed.sql
  • data/nigeria_wards_seed.sql
  • (optional) data/states-and-lgas-and-wards.json
"""

import json
import pathlib
import urllib.request
import datetime

URL = (
    "https://raw.githubusercontent.com/afeibukun/"
    "nigerian-state-lgas-wards-polling-units/"
    "main/states-and-lgas-and-wards.json"
)

# ──────────────────────────────────────────────────────────────
# Ensure data/ exists
# ──────────────────────────────────────────────────────────────
data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
data_dir.mkdir(exist_ok=True)

# (Optional) also save the raw JSON for reference
raw = urllib.request.urlopen(URL).read().decode()
(data_dir / "states-and-lgas-and-wards.json").write_text(raw, encoding="utf-8")
data = json.loads(raw)

# ──────────────────────────────────────────────────────────────
# Build rows
# ──────────────────────────────────────────────────────────────
state_rows, lga_rows, ward_rows = [], [], []
state_id = lga_id = 0
ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for state in data:
    state_id += 1
    state_name = state["state"].title()
    state_rows.append(
        f"({state_id},'{state_name}','enabled','{ts}','{ts}')"
    )

    for lga in state["lgas"]:
        lga_id += 1
        lga_name = lga["lga"].replace("-", " ").title()
        lga_rows.append(
            f"({lga_id},{state_id},'{lga_name}','enabled','{ts}','{ts}')"
        )

        for ward in lga["wards"]:
            ward_name = ward.replace("'", "''").replace("-", " ").title()
            ward_rows.append(
                f"({lga_id},'{ward_name}','enabled','{ts}','{ts}')"
            )

# ──────────────────────────────────────────────────────────────
# Write to SQL files in data/
# ──────────────────────────────────────────────────────────────
def write(name, cols, rows):
    path = data_dir / name
    path.write_text(
        "INSERT INTO `{}` ({}) VALUES\n".format(
            name.split("_")[1],
            ",".join(f"`{c}`" for c in cols),
        )
        + ",\n".join(rows)
        + ";\n",
        encoding="utf-8",
    )

write(
    "nigeria_states_seed.sql",
    ("id", "name", "status", "created_at", "updated_at"),
    state_rows,
)
write(
    "nigeria_lgas_seed.sql",
    ("id", "state_id", "name", "status", "created_at", "updated_at"),
    lga_rows,
)
write(
    "nigeria_wards_seed.sql",
    ("lga_id", "name", "status", "created_at", "updated_at"),
    ward_rows,
)

print(f"✓ wrote SQL files to {data_dir} ({len(state_rows)} states, "
      f"{len(lga_rows)} LGAs, {len(ward_rows)} wards)")
