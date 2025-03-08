from flask import Flask, render_template, request, jsonify
import textstat

app = Flask(__name__)

@app.route('/')
def home():
    print("Rendering index.html")
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    essay = data.get("essay", "")

    # Basic feedback generation
    content_feedback = "Your essay is well-structured." if len(essay) > 100 else "Consider expanding your essay."
    grammar_feedback = "No major grammar issues detected."  # You can integrate a grammar check here
    engagement_score = textstat.flesch_reading_ease(essay) // 10  # Normalized score

    return jsonify({
        "feedback": {
            "content_feedback": content_feedback,
            "grammar_feedback": grammar_feedback,
            "engagement_score": engagement_score
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
