from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Team03: Ieung </title>
            <style>
                body { font-family: Arial, sans-serif; }
                label { display: inline-block; width: 140px; }
                input[type="text"], select { padding: 8px; margin: 6px 0; box-sizing: border-box; display: inline-block; }
                input[type="radio"], input[type="checkbox"] { margin-right: 10px; }
                input[type="submit"] { margin-top: 20px; padding: 10px 20px; display: block; }
                .form-group { margin-bottom: 15px; }
                .email-group { align-items: center; }
                .email-group input[type="text"] { width: auto; flex: 1; }
                .email-group span { margin: 0 10px; }
            </style>
        </head>
        <body>
            <h1>Team03: Ieung </h1>
            <form action="/submit" method="post">
                <div class="form-group">
                    <label for="name">* Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="student_number">* Student Number</label>
                    <input type="text" id="student_number" name="student_number" required>
                </div>
                <div class="form-group">
                    <label for="university">* University</label>
                    <input type="text" id="university" name="university" required>
                </div>
                <div class="form-group">
                    <label for="major">* Major</label>
                    <input type="text" id="major" name="major" required>
                </div>
                <div class="form-group">
                    <label>* Gender</label>
                    <input type="radio" id="male" name="gender" value="Male" required>
                    <label for="male">Male</label>
                    <input type="radio" id="female" name="gender" value="Female" required>
                    <label for="female">Female</label>
                </div>
                <div class="form-group email-group">
                    <label for="email">* Email</label>
                    <input type="text" id="email" name="email" required>
                    <span>@</span>
                    <select name="email_domain">
                        <option value="example.com">선택</option>
                        <option value="gmail.com">gmail.com</option>
                        <option value="naver.com">naver.com</option>
                        <option value="amazon.com">amazon.com</option>
                        <option value="daum.net">daum.net</option>
                        <option value="dgu.edu">dgu.edu</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>* Programming Languages</label>
                    <input type="checkbox" id="python" name="languages" value="Python">
                    <label for="python">Python</label>
                    <input type="checkbox" id="java" name="languages" value="Java">
                    <label for="java">Java</label>
                    <input type="checkbox" id="html" name="languages" value="HTML">
                    <label for="html">HTML</label>
                    <input type="checkbox" id="cpp" name="languages" value="C++">
                    <label for="cpp">C++</label>
                </div>
                <input type="submit" value="submit">
            </form>
        </body>
        </html>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    student_number = request.form['student_number']
    university = request.form['university']
    major = request.form['major']
    gender = request.form['gender']
    email = request.form['email'] + '@' + request.form['email_domain']
    languages = request.form.getlist('languages')

    return f'''
        <h1>Submitted Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Student Number:</strong> {student_number}</p>
        <p><strong>University:</strong> {university}</p>
        <p><strong>Major:</strong> {major}</p>
        <p><strong>Gender:</strong> {gender}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Programming Languages:</strong> {', '.join(languages)}</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
