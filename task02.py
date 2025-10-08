import request 
import cvs
"""Get api usando request.
 1. get api y print codigo de estado
 2. checker respuesta, parsear a json, devuelve list de dict
 3.
 """


def fetch_and_print_posts():
    
    response = request.get(https://jsonplaceholder.typicode.com/posts)
    
    if response.status_code == 200:
        post = response.json()
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        with open("post.csv", "w", newline="", encoding= "utf-8") as csvf:
            writer = csv.DictWriter(csvf, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
