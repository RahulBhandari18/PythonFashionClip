import requests
# shaped rank --model-name movieRecs --user-id 295 --limit 5
# shaped similar --model-name movieRecs --item-id 493 --limit 5
# shaped similar --model-name movieRecs --user-id 295

API_KEY = "AEhf3Sy76i33Hsw48WJgA8ymQwQ6k5ho31Fzvhhw"
MODEL_URI = "https://api.shaped.ai/v1/models/movieRecs"
DATASET_URI = "https://api.shaped.ai/v1/datasets/events"
MODEL_ID = "movieRecs"
USER_ID = "295"

def get_recommendations(user_id):
    url = f"https://api.shaped.ai/rank/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"user_id": user_id, "num_results": 5}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    recommendations = get_recommendations(USER_ID)
    print("Recommendations:", recommendations)
