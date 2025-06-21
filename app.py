from flask import Flask, render_template, request, redirect
from ai_writer import generate_ai_text
from vector_store import save_to_store, search_versions

import os

app = Flask(__name__)
UPLOAD_FOLDER = "inputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        with open("inputs/original_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        return redirect("/rephrase")
    return render_template("index.html")

@app.route("/rephrase")
def rephrase():
    with open("inputs/original_text.txt", "r", encoding="utf-8") as f:
        original = f.read()
    rewritten = generate_ai_text(original)
    with open("outputs/final_version.txt", "w", encoding="utf-8") as f:
        f.write(rewritten)
    return render_template("review.html", original=original, rewritten=rewritten)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        results = search_versions(query, top_k=3, return_data=True)
        return render_template("results.html", results=results, query=query)
    return render_template("results.html", results=[])

if __name__ == "__main__":
    app.run(debug=True)
