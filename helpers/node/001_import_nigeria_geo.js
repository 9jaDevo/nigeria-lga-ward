// knex migrate:latest
const fs = require('fs');
const path = require('path');

exports.up = async function (knex) {
    const dataDir = path.join(__dirname, '..', '..', 'data');
    for (const file of ['nigeria_states_seed.sql', 'nigeria_lgas_seed.sql', 'nigeria_wards_seed.sql']) {
        await knex.raw(fs.readFileSync(path.join(dataDir, file), 'utf8'));
    }
};

exports.down = async function () {
    /* no-op */
};
