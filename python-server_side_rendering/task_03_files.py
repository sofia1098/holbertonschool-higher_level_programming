from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_products():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return []


def load_csv_products():
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        pass
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source == "json":
        data = load_json_products()
    elif source == "csv":
        data = load_csv_products()
    else:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=[])

    # Optional filtering by id
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]

            if not filtered:
                return render_template("product_display.html",
                                       error="Product not found",
                                       products=[])
            data = filtered

        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID",
                                   products=[])

    return render_template("product_display.html",
                           error=None,
                           products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
