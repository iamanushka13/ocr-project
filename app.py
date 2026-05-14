from flask import Flask, render_template, request
import os
from ocr import extract_text

app = Flask(__name__)

# IMPROVEMENT 1: Flask needs images to be in the "static" folder to display them on the web.
UPLOAD_FOLDER = "static/uploads" 
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# IMPROVEMENT 2: Automatically create the folder if it doesn't exist to prevent crash on first run
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    filepath = None  # <--- THE FIX: Initialize filepath before the 'if' statement
    
    if request.method == "POST":
        file = request.files["image"]
        
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            
            text = extract_text(filepath)
    
    # Now, if it's a GET request, filepath is safely 'None'
    return render_template("index.html", extracted_text=text, image_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)