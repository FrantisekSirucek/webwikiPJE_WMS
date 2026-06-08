const jwt = require('jsonwebtoken');

exports.handler = async (event, context) => {
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' }),
        };
    }

    const { username, password } = JSON.parse(event.body);

    // Zde můžete přidávat další uživatele do seznamu
    const users = [
        { username: 'PJExpediswiki', password: 'chcisetonaucit' },
        { username: 'externi_pristup', password: 'chciznatjakFungujeWMS' },
        // Příklad dalšího uživatele: odkomentujte a upravte podle potřeby
        // { username: 'novy_uzivatel', password: 'tajuplneheslo123' }
    ];

    const validUser = users.find(u => u.username === username && u.password === password);

    if (validUser) {
        const token = jwt.sign(
            { username },
            'PJExpedisWMS2024', // Tajný klíč
            { expiresIn: '1d' } // Platnost tokenu 1 den
        );

        console.log('Vygenerovaný token:', token);

        return {
            statusCode: 200,
            body: JSON.stringify({ token }),
        };
    } else {
        return {
            statusCode: 401,
            body: JSON.stringify({ error: 'Invalid credentials' }),
        };
    }
};
