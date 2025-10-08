import requests
import csv
"""Get api usando requests.
 1. get api y print codigo de estado
 2. checker respuesta, parsear a json, devuelve list de dict
 3.
 """


def fetch_and_print_posts():
    
    response = request.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in posts]

        with open("posts.csv", "w", newline="", encoding= "utf-8") as csvf:
            writer = csv.DictWriter(csvf, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
