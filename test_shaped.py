import requests
import os

# shaped create-model --file styl_model.yaml
# shaped update-model --file styl_model.yaml
# shaped delete-model --model-name styl_test
# shaped view-model --model-name styl_test
# shaped list-models

# shaped rank --model-name styl_test --user-id KLMNO --limit 5
# shaped similar --model-name styl_test --item-id 5 --limit 5
# shaped similar --model-name styl_test --user-id KLMNO

API_KEY = "AEhf3Sy76i33Hsw48WJgA8ymQwQ6k5ho31Fzvhhw"
MODEL_ID = "styl_test"

def get_recommendations(user_id):
    url = f"https://api.shaped.ai/rank/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"user_id": user_id, "num_results": 5}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    recommendations = get_recommendations(USER_ID)
    print("Recommendations:", recommendations)
