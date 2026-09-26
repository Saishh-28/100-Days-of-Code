from datetime import datetime
import requests

# ==================================================

# USER DATA

# ==================================================

GENDER = "female"
WEIGHT_KG = 68
HEIGHT_CM = 162
AGE = 18

# ==================================================

# NUTRITION API

# ==================================================

APP_ID = "app_cacbeb39bf394563b879c86e"
API_KEY = "nix_live_onif6zCBANmbD4LAGHm72aGXFLqHUNKf"

EXERCISE_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

nutrition_headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
"Content-Type": "application/json"
}

# ==================================================

# SHEETY

# ==================================================

SHEETY_ENDPOINT = "https://api.sheety.co/ccfec359490ab89d08fd7c9d669f729b/workout/workouts"

SHEETY_USERNAME = "Saisha_28"
SHEETY_PASSWORD = "MyGYMtracker@28"

# ==================================================

# INPUT

# ==================================================

exercise_text = input("Tell me which exercises you did: ")

# Example:

# "5km walk and 30 situps and cycled for 20 minutes"

exercise_queries = exercise_text.lower().split(" and ")

# ==================================================

# DATE & TIME

# ==================================================

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%H:%M:%S")

# ==================================================

# PROCESS EACH EXERCISE

# ==================================================

for query in exercise_queries:


    exercise_params = {
        "query": query.strip(),
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    response = requests.post(
        EXERCISE_ENDPOINT,
        headers=nutrition_headers,
        json=exercise_params
    )

    response.raise_for_status()

    result = response.json()

    for exercise in result["exercises"]:

        sheet_data = {
            "workout": {
                "date": today,
                "time": now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        sheet_response = requests.post(
            SHEETY_ENDPOINT,
            json=sheet_data,
            auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
        )

        sheet_response.raise_for_status()

        print(
            f"✅ Added: {exercise['name'].title()} | "
            f"{exercise['duration_min']} min | "
            f"{exercise['nf_calories']} calories"
        )


print("\n🎉 Workout successfully logged to Google Sheets!")
