def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }


# REKOGNITION
#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

# import boto3

# if __name__ == "__main__":

#     sourceFile='source.jpg'
#     targetFile='target.jpg'
#     client=boto3.client('rekognition')
   
#     imageSource=open(sourceFile,'rb')
#     imageTarget=open(targetFile,'rb')

#     response=client.compare_faces(SimilarityThreshold=70,
#                                   SourceImage={'Bytes': imageSource.read()},
#                                   TargetImage={'Bytes': imageTarget.read()})
    
#     for faceMatch in response['FaceMatches']:
#         position = faceMatch['Face']['BoundingBox']
#         confidence = str(faceMatch['Face']['Confidence'])
#         print('The face at ' +
#                str(position['Left']) + ' ' +
#                str(position['Top']) +
#                ' matches with ' + confidence + '% confidence')

#     imageSource.close()
#     imageTarget.close()               



# TEXTRACT
# import boto3

# def analyze_id(client, bucket_name, file_name):

#     # Analyze document
#     # process using S3 object
#     response = client.analyze_id(
#         DocumentPages=[{'S3Object': {'Bucket': bucket_name, 'Name': file_name}}])

#     for doc_fields in response['IdentityDocuments']:
#         for id_field in doc_fields['IdentityDocumentFields']:
#             for key, val in id_field.items():
#                 if "Type" in str(key):
#                     print("Type: " + str(val['Text']))
#             for key, val in id_field.items():
#                 if "ValueDetection" in str(key):
#                     print("Value Detection: " + str(val['Text']))
#             print()

# def main():
#     session = boto3.Session(profile_name='profile-name')
#     client = session.client('textract', region_name='region')
#     bucket_name = "bucket"
#     file_name = "file"

#     analyze_id(client, bucket_name, file_name)

# if __name__ == "__main__":
#     main()