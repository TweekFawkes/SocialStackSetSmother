import json
import socket
import boto3
import time
# import requests

def lambda_handler(event, context):
    sReturn = "NULL"
    #
    sBucket = 'TODO_S3_BUCKET_NAME' # already created on S3
    #
    try:
        sTimeStamp = str( time.strftime('%Y%m%d%H%M%S') )
        oBody = event['body']
        sBody = str(oBody)
        #
        sFileName = sTimeStamp + "_reg.txt"
        client = boto3.client('s3')
        client.put_object(Body=sBody, Bucket=sBucket, Key=sFileName)
        #
        sReturn = str(sBody)
    except Exception as e:
        print("[!] Exception (e):" + str(e))
        sReturn = str(e)
    #
    return {
        "statusCode": 200,
        #"body": sReturn,
        "body": json.dumps({
            "message": sReturn
        }),
    }