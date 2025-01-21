const jwt = require('jsonwebtoken');

exports.handler = async (event, context) => {
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' }),
        };
    }

    const { username, password } = JSON.parse(event.body);

    // Pevně nastavené přihlašovací údaje
    const validUsername = 'test';
    const validPassword = 'test';

    if (username === validUsername && password === validPassword) {
        const token = jwt.sign(
            { username },
            'PJExpedisSecretKey', // Tajný klíč pro token
            { expiresIn: '1d' }   // Platnost tokenu
        );

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
