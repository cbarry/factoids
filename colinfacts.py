import string

def lambda_handler(event, context):
    return {
        "version": "1.0",
        "sessionAttributes": {
            },
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Colin says hi"
                },
        "shouldEndSession": True
        }
    }
