from flask import Flask,render_template
app = Flask(__name__)

#플라스크 메인 페이지
@app.route("/")
def main():
    return render_template('index.html')
#회원가입 페이지
@app.route("/signup") 
def signup():
    return render_template('membership.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
