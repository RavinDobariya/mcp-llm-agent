import requests
from app.config.settings import SERP_API_KEY


async def perform_search(query: str) -> str:
    url = "https://serpapi.com/search"

    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "organic_results" not in data:
        return "No results found."

    results = data["organic_results"][:5]

    formatted = []

    for r in results:
        title = r.get("title", "No title")
        link = r.get("link", "")
        snippet = r.get("snippet", "")
        formatted.append(f"{title}\n{snippet}\n{link}\n")

    return "\n".join(formatted)