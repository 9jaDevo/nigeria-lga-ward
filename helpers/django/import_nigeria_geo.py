from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path

class Command(BaseCommand):
    help = "Import Nigeria state/LGA/ward seed SQL"

    def handle(self, *args, **opts):
        cursor = connection.cursor()
        base = Path(__file__).resolve().parent.parent.parent / "data"
        for file in ["nigeria_states_seed.sql", "nigeria_lgas_seed.sql", "nigeria_wards_seed.sql"]:
            cursor.execute(Path(base / file).read_text())
        self.stdout.write(self.style.SUCCESS("All seed data imported."))
