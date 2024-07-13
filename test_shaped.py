import requests
import os

# shaped rank --model-name styl --user-id KLMNO --limit 5
# shaped similar --model-name styl --item-id 5 --limit 5
# shaped similar --model-name styl --user-id KLMNO

API_KEY = "AEhf3Sy76i33Hsw48WJgA8ymQwQ6k5ho31Fzvhhw"
SHAPED_API_KEY = os.getenv('TEST_SHAPED_API_KEY', API_KEY)
MODEL_URI = "https://api.shaped.ai/v1/models/styl"
DATASET_URI = "https://api.shaped.ai/v1/datasets/events"
MODEL_ID = "styl"
# USER_ID = "ABCDE"
# USER_ID = "FGHIJ"
USER_ID = "KLMNO"

def get_recommendations(user_id):
    url = f"https://api.shaped.ai/rank/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"user_id": user_id, "num_results": 5}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    recommendations = get_recommendations(USER_ID)
    print("Recommendations:", recommendations)
