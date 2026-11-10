from flask import Flask, render_template

app = Flask(__name__)

tools = [
    {"slug": "age-calculator", "name": "Age Calculator", "icon": "🎂"},
    {"slug": "word-counter", "name": "Word Counter", "icon": "📝"},
    {"slug": "password-generator", "name": "Password Generator", "icon": "🔑"},
]

@app.route('/')
def home():
    return render_template('index.html', tools=tools)

@app.route('/tool/<slug>/')
def tool_page(slug):
    tool = next((t for t in tools if t["slug"] == slug), tools[0])
    return render_template('tool.html', tool=tool)

if __name__ == '__main__':
    app.run(debug=True)