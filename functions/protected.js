const jwt = require('jsonwebtoken');

exports.handler = async (event, context) => {
    const token = event.headers.authorization?.split(' ')[1];

    if (!token) {
        return {
            statusCode: 401,
            body: JSON.stringify({ error: 'No token provided' }),
        };
    }

    try {
        const decoded = jwt.verify(token, 'PJExpedisWMS2024');
        console.log('Token valid:', decoded);
        return {
            statusCode: 200,
            body: JSON.stringify({ message: 'Token is valid', user: decoded }),
        };
    } catch (error) {
        console.error('Chyba při ověřování tokenu:', error);
        return {
            statusCode: 401,
            body: JSON.stringify({ error: 'Invalid token' }),
        };
    }
};
