from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_nutrition():
    data = request.form
    weight = float(data['weight'])
    height = float(data['height'])
    # Simple example calculation
    calories_needed = weight * 25  # You should replace this with actual nutritional logic
    
    return jsonify({"caloriesNeeded": calories_needed})

if __name__ == '__main__':
    app.run(debug=True)