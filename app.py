from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET'])
def uploader():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('uploads/' + file.filename)
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True, port=1199, host="0.0.0.0")