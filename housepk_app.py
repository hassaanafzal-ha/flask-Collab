from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to House PK Application",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# dev 2
@app.route('/dashboard')
def dashboard():
    print("Dashboard accessed by user")
    return jsonify({
        "message": "Welcome to Dashboard",
        "data": {
            "total_properties": 150,
            "new_listings": 12
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

