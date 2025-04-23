# 🇳🇬 Nigeria States → LGAs → Wards – Ready-to-import MySQL seed files

**37 states, 774 local‐government areas, ~8 800 wards** — packaged as three SQL files you can drop straight into MySQL, MariaDB, Laravel, WordPress, Django, Node/Knex, or even a one-shot Docker stack.

> **Repo:** **`nigeria-lga-ward`** ·  
> **Data version:** auto-generated weekly from the latest open JSON  
> **License:** Code MIT | Data CC‑BY 4.0 © afeibukun

---

## 🔗 Quick import

```bash
git clone https://github.com/9jaDevo/nigeria-lga-ward.git
cd nigeria-lga-ward/data

mysql -u root -p yourdb < nigeria_states_seed.sql
mysql -u root -p yourdb < nigeria_lgas_seed.sql
mysql -u root -p yourdb < nigeria_wards_seed.sql
```

Done — your database now contains the full administrative hierarchy with `state_id` ↔ `lga_id` ↔ `ward` relationships already wired.

> **Table shapes**

| Table    | Primary key | Foreign key | Columns                                                |
| -------- | ----------- | ----------- | ------------------------------------------------------ |
| `states` | `id`        | –           | id, name, status, created_at, updated_at               |
| `lgas`   | `id`        | `state_id`  | id, **state_id**, name, status, created_at, updated_at |
| `wards`  | –           | `lga_id`    | **lga_id**, name, status, created_at, updated_at       |

---

## 📚 Language-specific helpers

| Stack / Tool        | Helper file                                | One‑liner to run                               |
| ------------------- | ------------------------------------------ | ---------------------------------------------- |
| Laravel 10          | `helpers/laravel/NigeriaGeoSeeder.php`     | `php artisan db:seed --class=NigeriaGeoSeeder` |
| WordPress           | `helpers/wordpress/nigeria-geo-import.php` | Upload & **Activate** plugin                   |
| Node.js + Knex      | `helpers/node/001_import_nigeria_geo.js`   | `knex migrate:latest`                          |
| Python + SQLAlchemy | `helpers/python/import_nigeria_geo.py`     | `python helpers/python/import_nigeria_geo.py`  |
| Django              | `helpers/django/import_nigeria_geo.py`     | `python manage.py import_nigeria_geo`          |
| Docker              | `helpers/docker-compose.yml`               | `docker compose up -d`                         |

Each helper assumes the three SQL files live in `data/` one level up. Adjust paths if you reorganise.

---

## ♻️  Re‑generate seed files

Need the freshest data or want to tweak columns? Run the generator:

```bash
python scripts/build_seeds.py
```

It:

1. Downloads the latest JSON from the upstream open‑data repo.  
2. Generates/overwrites  
   * `nigeria_states_seed.sql`  
   * `nigeria_lgas_seed.sql`  
   * `nigeria_wards_seed.sql`  
3. Updates timestamps to **NOW()** for reproducible imports.

### Continuous updates (GitHub Actions)

We ship `.github/workflows/build.yml` that rebuilds and commits fresh SQL every Monday at 02:00 UTC. Disable or change the schedule to taste.

---

## 🗂  Folder layout

```
data/                   # three ready-to-import SQL files + source JSON snapshot
scripts/
    build_seeds.py      # Python generator (no DB credentials required)
helpers/
    laravel/…           # NigeriaGeoSeeder.php
    wordpress/…         # one-click import plugin
    node/…              # Knex migration
    python/…            # pure SQLAlchemy script
    django/…            # Django management command
    docker-compose.yml  # MySQL 8 + Adminer demo stack
.github/
    workflows/build.yml # CI to auto-refresh weekly
README.md
LICENSE                 # MIT for code
```

---

## 📑 Licensing & attribution

| Item                                    | License   | Notes                                                                                                                      |
| --------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Seed generator & helpers (all code)** | MIT       | Free for personal and commercial use, no warranty.                                                                         |
| **Seed data (`*.sql`, JSON snapshot)**  | CC‑BY 4.0 | Attribution required. Source JSON © **afeibukun** → <https://github.com/afeibukun/nigerian-state-lgas-wards-polling-units> |

Please keep the attribution line intact when you redistribute or publish derivative data sets.

---

## 🙌  Contributing

Spotted a misspelling, boundary change, or new ward? Open an issue or PR:

1. Edit the JSON snapshot in `data/` **or** improve `build_seeds.py` so it handles the change automatically.  
2. Run `python scripts/build_seeds.py`.  
3. Commit the updated JSON and regenerated SQL.

---

## ⭐  Give it a star & share!

If this repo saved you time, hit ⭐ and share the link in Nigerian dev communities, Laravel/WordPress Slack, or wherever your peers hang out.

Happy coding!
