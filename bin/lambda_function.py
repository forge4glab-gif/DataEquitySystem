import json
import boto3
import time
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DataEquity_Master_Index')

def lambda_handler(event, context):
    # Captura o IP real da conexão (IPv4 ou IPv6)
    ip_detectado = event.get('requestContext', {}).get('http', {}).get('sourceIp', 'IP_NAO_DETECTADO')
    
    # Gera o carimbo de tempo e ID oficial
    agora = datetime.utcnow().isoformat()
    deq_id = f"DEQ-{int(time.time() * 1000)}"
    
    # Tenta capturar o IMEI de várias formas possíveis (Flexibilidade de Auditoria)
    corpo = {}
    if event.get('body'):
        try: corpo = json.loads(event['body'])
        except: pass
    
    imei = corpo.get('device_imei') or corpo.get('imei') or corpo.get('ID') or "S25FE_VINCULADO_POR_IP"

    # Gravação Definitiva para INPI e Monetização
    table.put_item(Item={
        'EventID': deq_id,
        'timestamp': agora,
        'source_ip': ip_detectado,
        'device_imei': imei,
        'status': 'AUDITADO_INPI',
        'valor_monetizacao': 1.0
    })
    
    return {'statusCode': 200, 'body': json.dumps({'Selo': 'INPI_OK', 'ID': deq_id})}
