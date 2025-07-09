import requests

NO_DATA = "No data"
API_KEY = "ENTER_YOUR_API_KEY"

query = input("Search for: ")

url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)
data = response.json()

results = data.get("results", [])

if not results:
    print("No results found.")
    exit()

for i, movie in enumerate(results, start=1):
    print(f"{i}. {movie.get('original_title', NO_DATA)}")

try:
    user_choice = int(input(f"Choose from 1-{len(results)}: "))
    selected = results[user_choice - 1]
except (ValueError, IndexError):
    print("❌ Invalid choice. Exiting.")
    exit()

print(f"""
🎬 Title: {selected.get("original_title", NO_DATA)}
📝 Description: {selected.get("overview", NO_DATA)}

📅 Release Date: {selected.get("release_date", NO_DATA)}
🌍 Language: {selected.get("original_language", NO_DATA)}
🔞 Adults only: {"Yes" if selected.get("adult", False) else "No"}
""")

