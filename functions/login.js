const jwt = require('jsonwebtoken');

exports.handler = async (event, context) => {
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' }),
        };
    }

    const { username, password } = JSON.parse(event.body);

    const validUsername = 'PJExpediswiki';
    const validPassword = 'chcisetonaucit';

    if (username === validUsername && password === validPassword) {
        const token = jwt.sign(
            { username },
            'PJExpedisWMS2024', // Tajný klíč
            { expiresIn: '1d' } // Platnost tokenu 1 den
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

const jwt = require('jsonwebtoken');

exports.handler = async (event, context) => {
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' }),
        };
    }

    const { username, password } = JSON.parse(event.body);

    const validUsername = 'PJExpediswiki';
    const validPassword = 'chcisetonaucit';

    if (username === validUsername && password === validPassword) {
        const token = jwt.sign(
            { username },
            'PJExpedisWMS2024', // Tajný klíč
            { expiresIn: '1d' } // Platnost tokenu 1 den
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
