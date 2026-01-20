from flask import Flask, render_template, request, redirect, url_for # type: ignore
import pickle
import numpy as np # type: ignore
import pandas as pd # type: ignore

app = Flask(__name__)

# Load model and encoders
model = pickle.load(open("models/college_model.pkl", "rb"))
encoders = pickle.load(open("models/feature_encoders.pkl", "rb"))
label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    top5 = None
    if request.method == "POST":
        branch = request.form["branch"]
        marks = float(request.form["marks"])
        caste = request.form["caste"]
        cap_round = int(request.form["cap_round"])
        status = request.form["status"]

        # Prepare input
        input_df = pd.DataFrame([{
            "branch": branch,
            "marks": marks,
            "caste": caste,
            "Cap_round_no": cap_round,
            "status": status
        }])

        # Encode
        for col in ["branch", "caste", "status"]:
            try:
                input_df[col] = encoders[col].transform(input_df[col])
            except ValueError:
                input_df[col] = [0]   # fallback

        # Prediction
        probs = model.predict_proba(input_df)[0]
        top_indices = np.argsort(probs)[::-1][:5]
        top5 = [(label_encoder.inverse_transform([i])[0], probs[i]) for i in top_indices]

    return render_template("about.html", top5=top5)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
