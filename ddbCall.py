import os
import boto3
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def getOpenAIKey():
    #Pull OpenAI API Key from DDB
    ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')
    logger.info(ddb_table_name)
    dynamodb = boto3.client('dynamodb')
    key = dynamodb.get_item(
        TableName=ddb_table_name,
        Key={
            'id': {
                'S': 'openAIKey'
                }
            }
    )
    apiKeyDDB = key['Item']['openAIKey']['S']
    logger.info(key)
    logger.info(apiKeyDDB)
    return apiKeyDDB