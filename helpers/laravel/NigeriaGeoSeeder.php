<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\File;

class NigeriaGeoSeeder extends Seeder
{
    public function run(): void
    {
        $files = [
            database_path('seed-data/nigeria_states_seed.sql'),
            database_path('seed-data/nigeria_lgas_seed.sql'),
            database_path('seed-data/nigeria_wards_seed.sql'),
        ];

        foreach ($files as $file) {
            DB::unprepared(File::get($file));
        }
    }
}
