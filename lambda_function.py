import json
import boto3
from PIL import Image
import  os


size = 256, 256
s3 = boto3.client('s3')


def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_name = record['s3']['object']['key']
        file_name = os.path.relpath(object_name, 'images')

        with open(f'/tmp/{file_name}.png', 'wb') as data:
            s3.download_fileobj(bucket_name, object_name, data)

        im = Image.open(f'/tmp/{file_name}.png')
        im.thumbnail(size)
        im.save(f'/tmp/{file_name}.thumbnail.png', "PNG")

        with open(f'/tmp/{file_name}.thumbnail.png', 'rb') as data:
            s3.upload_fileobj(data, bucket_name, f'thumbnails/{file_name}.thumbnail.png')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
