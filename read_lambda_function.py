import json
import boto3
def lambda_handler(event, context):
  
  dynamodb = boto3.resource('dynamodb')
  tableRsuAccidentSignals = dynamodb.Table('RsuAccidentSignals')
  response = tableRsuAccidentSignals.scan()
  return {
    'statusCode': 200,
    'body': response['Items']
  }