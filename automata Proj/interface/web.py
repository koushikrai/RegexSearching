from flask import Flask, request, render_template
from regex_engine.search import search_documents

app = Flask(__name__)  # Adjust the path as necessary

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        # Get the regex pattern and folder path from the form
        regex = request.form["regex"]
        folder = request.form["folder"]
        
        # Perform the regex search
        results = search_documents(regex, folder)
    
    # Render the template with the results
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=False)
