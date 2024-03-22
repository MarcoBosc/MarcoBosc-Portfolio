import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    id_image = body["id_image"]
    face_image = body["face"]
    name = body["firstName"]
    birth = body["birth"]
    rg = body["rg"]
    cpf = body["cpf"]
    
    extracted_data = {
        'nome': False,
        'birth': False,
        'rg': False,
        'cpf': False
    }

    def rekognition(face_image, id_image):
        confidence = 0
        client = boto3.client('rekognition')
        
        source_image_bytes = face_image
        target_image_bytes = id_image

        response = client.compare_faces(
            SimilarityThreshold=70,
            SourceImage={'Bytes': source_image_bytes},
            TargetImage={'Bytes': target_image_bytes}
        )

        for faceMatch in response['FaceMatches']:
            confidence = str(faceMatch['Face']['Confidence'])
        
        return float(confidence) >= 90

    def textract(name, birth, rg, cpf):
        session = boto3.Session(profile_name='default')
        client = session.client('textract', region_name='us-east-1')
        
        response = client.analyze_document(
            Document={
                'Bytes': id_image
            },
            FeatureTypes=['FORMS']
        )
    
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                text = item["Text"]
                if name in text:
                    extracted_data['nome'] = True
                if birth in text:
                    extracted_data['birth'] = True
                if rg in text:
                    extracted_data['rg'] = True
                if cpf in text:
                    extracted_data['cpf'] = True

        all_fields_found = all(extracted_data.values())
        if all_fields_found:
            return True
        else:
            return False
        
    if rekognition(face_image, id_image) and textract(name, birth, rg, cpf):
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': {
                'verified': True
            }
        }
