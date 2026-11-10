from flask import Flask, render_template,send_from_directory

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
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml', mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
