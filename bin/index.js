const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,POST"
    };
    try {
        const body = JSON.parse(event.body);
        const novoToken = "USER-" + Math.random().toString(36).substr(2, 8).toUpperCase();
        const params = {
            TableName: "DataEquity_Users",
            Item: {
                "user_id": novoToken,
                "device_id": "WAITING_FIRST_LOGIN",
                "Nome": body.nome,
                "Email": body.email,
                "Nivel": "Perito",
                "Status": "Ativo",
                "DataCadastro": new Date().toISOString().split('T')[0],
                "SaldoTotal": 0.00
            }
        };
        await dynamo.put(params).promise();
        return {
            statusCode: 200,
            headers: headers,
            body: JSON.stringify({ success: true, token: novoToken })
        };
    } catch (err) {
        return { statusCode: 500, headers: headers, body: JSON.stringify({ success: false, error: err.message }) };
    }
};
