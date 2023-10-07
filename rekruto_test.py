from flask import Flask, request, render_template_string

app = Flask(__name__)

# Шаблон страницы
template = """
Hello {{ name }}!
{{ message }}!
"""

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'Unknown')
    message = request.args.get('message', '')
    return render_template_string(template, name=name, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#http://127.0.0.1:5000/?name=Rekruto&message=Давай%20дружить!
