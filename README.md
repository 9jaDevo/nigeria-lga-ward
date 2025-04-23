# nigeria-lga-ward
 Ready-to-import MySQL seed files for Nigeria — 37 states, 774 LGAs, 8 800 + wards (auto-generated from open data)

## Language-specific helpers  📚

| Stack | Helper | How to run |
|-------|--------|-----------|
| Laravel 10 | `helpers/laravel/NigeriaGeoSeeder.php` | `php artisan db:seed --class=NigeriaGeoSeeder` |
| WordPress | `helpers/wordpress/nigeria-geo-import.php` | Upload & activate plugin |
| Node.js (Knex) | `helpers/node/001_import_nigeria_geo.js` | `knex migrate:latest` |
| Python / SQLAlchemy | `helpers/python/import_nigeria_geo.py` | `python import_nigeria_geo.py` |
| Django | `helpers/django/import_nigeria_geo.py` | `python manage.py import_nigeria_geo` |
| Docker quick-start | `helpers/docker-compose.yml` | `docker compose up -d` |