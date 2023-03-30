import json

def lambda_handler(event, context):
    message = "Hello, GIM!, What's up people?"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
