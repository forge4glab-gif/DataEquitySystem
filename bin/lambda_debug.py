import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log crucial para a perícia: Mostra TUDO o que chega
    logger.info("--- EVENTO RECEBIDO PELO S25 FE ---")
    logger.info(json.dumps(event))
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Dados recebidos para auditoria INPI', 'status': 'CAPTURED'})
    }
