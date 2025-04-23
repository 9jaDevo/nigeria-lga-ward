<?php
/*
 * Plugin Name: Nigeria Geo Import
 * Plugin URI: https://github.com/9jaDevo/nigeria-lga-ward
 * Description: One-click import of states, LGAs & wards.
 * Version: 1.0.0
 * Author: Michael Akinwumi
 * Author URI: https://michaelakinwumi.com/
*/

register_activation_hook(__FILE__, 'ngi_run_import');

function ngi_run_import()
{
    global $wpdb;

    $dir  = plugin_dir_path(__FILE__) . '../data/';
    $sqls = ['nigeria_states_seed.sql', 'nigeria_lgas_seed.sql', 'nigeria_wards_seed.sql'];

    foreach ($sqls as $sql) {
        $wpdb->query(file_get_contents($dir . $sql));
    }
}
