import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers for the API request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Create the input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the API
    response = requests.post(url, headers=headers, json=input_json)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        emotions = result['emotionPredictions'][0]['emotion']

        # Extract emotion scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        # Find dominant emotion
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(scores, key=scores.get)

        # Return the structured dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    else:
        if response.status_code == 400:
            # Return all values as None for blank input
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            print("❌ API call failed")
            print(f"Status Code: {response.status_code}")
            print("Response Text:", response.text)
            return None
