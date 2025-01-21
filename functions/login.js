const sqlite3 = require('sqlite3').verbose();
const jwt = require('jsonwebtoken');

exports.handler = async (event, context) => {
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' }),
        };
    }

    const { username, password } = JSON.parse(event.body);

    if (!username || !password) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Missing credentials' }),
        };
    }

    // Připojení k databázi
    const db = new sqlite3.Database('./database.db');

    return new Promise((resolve, reject) => {
        db.get(
            'SELECT * FROM users WHERE username = ?',
            [username],
            (err, row) => {
                if (err) {
                    reject({
                        statusCode: 500,
                        body: JSON.stringify({ error: 'Database error' }),
                    });
                }

                if (row && row.password_hash === password) {
                    const token = jwt.sign(
                        { id: row.id, username: row.username },
                        'PJExpedisWMS2024', // Secret key
                        { expiresIn: '1d' }
                    );

                    resolve({
                        statusCode: 200,
                        body: JSON.stringify({ token, username: row.username }),
                    });
                } else {
                    resolve({
                        statusCode: 401,
                        body: JSON.stringify({ error: 'Invalid credentials' }),
                    });
                }
            }
        );
    }).finally(() => {
        db.close();
    });
};
