import requests
import csv

"""Get API usando requests.
 1. Hacer GET y mostrar código de estado
 2. Si la respuesta es exitosa, parsear a JSON (lista de diccionarios)
 3. Mostrar los títulos de los posts
 4. Guardar en un CSV con id, title y body
"""

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])   # mostramos el título de cada post

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvf:
            writer = csv.DictWriter(csvf, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
