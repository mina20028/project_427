from flask import Flask, render_template_string, request, redirect, url_for, flash,session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
patients = {
    "159": {"name": "John Doe", "age": 30, "checkpoint": "Checkup", "image": "download (3).jpeg", "report": "", "report_saved": False},
    "160": {"name": "Jane Smith", "age": 25, "checkpoint": "Follow-up", "image": "download.jpeg", "report": "", "report_saved": False},
    "161": {"name": "Alice Brown", "age": 40, "checkpoint": "Diagnosis", "image": "download (1).jpeg", "report": "", "report_saved": False},
    "162": {"name": "Mena Magdy", "age": 22, "checkpoint": "Diseases", "image": "4.jpeg", "report": "", "report_saved": False},
    "163": {"name": "Youssef Rafat", "age": 23, "checkpoint": "Salts", "image": "5.jpeg", "report": "", "report_saved": False},
    "164": {"name": "Ahmed Ashraf", "age": 40, "checkpoint": "Sugar", "image": "images.jpeg", "report": "", "report_saved": False}
}

users = {"doc": "password123"}


@app.route('/', methods=['GET', 'POST'])
def patient_table():
    if 'username' not in session:
        return redirect(url_for('login'))
    search_query = request.form.get('search', '').lower()
    filtered_patients = {id: p for id, p in patients.items() if search_query in p['name'].lower()}

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>جدول معلومات المرضى</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            .navbar {
                background-color: #0056b3;
                padding: 10px;
                text-align: center;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            .navbar a {
                color: white;
                text-decoration: none;
                padding: 14px 20px;
                font-size: 18px;
            }
            .navbar a:hover {
                background-color: #004494;
                border-radius: 5px;
            }
            .navbar form {
                display: inline-block;
                margin: 0;
                padding: 0;
            }
            .navbar input[type="text"] {
                padding: 7px;
                border-radius: 5px;
                border: 1px solid #ddd;
                font-size: 16px;
            }
            .navbar button {
                padding: 7px 15px;
                border: none;
                border-radius: 5px;
                background-color: #004494;
                color: white;
                cursor: pointer;
            }
            h1 {
                text-align: center;
                color: #0056b3;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            table, th, td {
                border: 1px solid #ddd;
            }
            th, td {
                padding: 12px;
                text-align: left;
            }
            th {
                background-color: #0056b3;
                color: #fff;
                text-transform: uppercase;
            }
            td {
                background-color: #fff;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
            a img {
                border-radius: 5px;
            }
            input[type="checkbox"] {
                transform: scale(1.5);
                margin-right: 10px;
            }
            .footer {
                background-color: #0056b3;
                color: #fff;
                padding: 40px 20px;
                text-align: center;
            }
            .footer-content {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                align-items: flex-start;
                margin-bottom: 20px;
            }
            .footer-logo img {
                margin-bottom: 20px;
            }
            .footer-links ul, .footer-insurances ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            .footer-links ul li, .footer-insurances ul li {
                margin: 5px 0;
            }
            .footer-links ul li a, .footer-insurances ul li a {
                color: #fff;
                text-decoration: none;
            }
            .footer-links ul li a:hover, .footer-insurances ul li a:hover {
                text-decoration: underline;
            }
            .footer-insurances h3, .footer-social h3 {
                margin-bottom: 10px;
            }
            .footer-social a img {
                width: 40px;
                margin: 0 10px;
            }
            .footer-bottom {
                border-top: 1px solid #fff;
                padding-top: 20px;
                margin-top: 20px;
            }
            .footer-bottom a {
                color: #fff;
                text-decoration: none;
            }
            .footer-bottom a:hover {
                text-decoration: underline;
            }
            .doctor-container {
                text-align: center;
                margin: 40px 0;
            }
            .doctor-container h2 {
                color: #0056b3;
                margin-bottom: 20px;
            }
            .doctor-box {
                display: inline-block;
                width: 30%;
                padding: 10px;
                margin: 0 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                background-color: #fff;
                border-radius: 10px;
            }
            .doctor-box img {
                width: 100%;
                border-radius: 10px;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="navbar">
            <a href="{{ url_for('patient_table') }}">Home</a>
            <a href="{{ url_for('patient_table') }}">Patients</a>
            <a href="{{ url_for('contact') }}">Contact</a>
        
        <a href="{{ url_for('logout') }}">Logout</a>
            <form method="post" action="{{ url_for('patient_table') }}">
                <input type="text" name="search" placeholder="Search for patient..." value="{{ request.form.get('search', '') }}">
                <button type="submit">Search</button>
            </form>
        </div>
        <h1>Information of Patients</h1>
        <table>
            <tr>
                <th>Name of Patient</th>
                <th>Age</th>
                <th>ID</th>
                <th>Check Point</th>
                <th>X-rays</th>
                <th>Saved Report</th>
            </tr>
            {% for patient_id, patient in filtered_patients.items() %}
            <tr>
                <td>{{ patient.name }}</td>
                <td>{{ patient.age }}</td>
                <td>{{ patient_id }}</td>
                <td>{{ patient.checkpoint }}</td>
                <td><a href="{{ url_for('patient_detail', patient_id=patient_id) }}"><img src="{{ url_for('static', filename='images/' + patient.image) }}" alt="Patient Image" width="100"></a></td>
                <td><input type="checkbox" {% if patient.report_saved %}checked{% endif %} disabled></td>
            </tr>
            {% endfor %}
        </table>
        
        <div class="doctor-container">
            <h2>Our Doctors</h2>
            <div class="doctor-box">
                <img src="{{ url_for('static', filename='images/d1.jpg') }}" alt="Doctor 1">
               
            </div>
            <div class="doctor-box">
                <img src="{{ url_for('static', filename='images/d2.jpg') }}" alt="Doctor 2">
                
            </div>
            <div class="doctor-box">
                <img src="{{ url_for('static', filename='images/d5.jpg') }}" alt="Doctor 3">
                
            </div>
        </div>

        <div class="footer">
            <div class="footer-content">
                
                <div class="footer-links">
                    <ul>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Annual Checkup</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Careers</a></li>
                        <li><a href="#">Get a Diagnosis</a></li>
                        <li><a href="#">Lab Tests</a></li>
                    </ul>
                </div>
                <div class="footer-insurances">
                    <h3>We accept:</h3>
                    <ul>
                        <li><a href="#">Allianz Insurance</a></li>
                        <li><a href="#">MetLife Insurance</a></li>
                        <li><a href="#">Cigna Insurance</a></li>
                    </ul>
                </div>
                <div class="footer-social">
                    <h3>Follow Us:</h3>
                    <a href="#"><img src="{{ url_for('static', filename='images/2023_Facebook_icon.svg (1).png') }}" alt="Facebook"></a>
                    <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1)..png') }}" alt="Instagram"></a>
                    <a href="#"><img src="{{ url_for('static', filename='images/download (2).png') }}" alt="Twitter"></a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Your Medical Center. All rights reserved.</p>
                <p><a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, filtered_patients=filtered_patients)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('patient_table'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('patient_table'))
        else:
            flash('Invalid credentials. Please try again.')

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .login-container {
                width: 350px;
                padding: 20px;
                background: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            .login-container h1 {
                text-align: center;
                margin-bottom: 20px;
            }
            .login-container label {
                display: block;
                margin: 10px 0 5px;
            }
            .login-container input {
                width: 95%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            .login-container button {
                width: 100%;
                padding: 10px;
                background: #007bff;
                color: #fff;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .login-container button:hover {
                background: #0056b3;
            }
            .alert {
                color: red;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h1>Login</h1>
            <form method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br>
                <button type="submit">Login</button>
            </form>
            {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="alert">
                    {{ messages[0] }}
                </div>
            {% endif %}
            {% endwith %}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/patient/<patient_id>', methods=['GET', 'POST'])
def patient_detail(patient_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    patient = patients.get(patient_id)
    if not patient:
        return "Patient not found", 404

    if request.method == 'POST':
        patient['report'] = request.form['report']
        patient['report_saved'] = True
    html = '''
    
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Patient Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            h2 {
                text-align: center;
                color: #0056b3;
            }
            .form-group {
                margin-bottom: 20px;
            }
            .form-group label {
                display: block;
                font-weight: bold;
                margin-bottom: 5px;
            }
            .form-group textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                resize: vertical;
            }
            .form-group button {
                background-color: #0056b3;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            .form-group button:hover {
                background-color: #004494;
            }
            .back-link {
                display: block;
                text-align: center;
                margin-top: 20px;
                text-decoration: none;
                color: #0056b3;
            }
            .back-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Patient Report - {{ patient.name }}</h2>
            <p><strong>ID:</strong> {{ patient_id }}</p>
            <p><strong>Name:</strong> {{ patient.name }}</p>
            <p><strong>Age:</strong> {{ patient.age }}</p>
            <p><strong>Check Point:</strong> {{ patient.checkpoint }}</p>
            <img src="{{ url_for('static', filename='images/' + patient.image) }}" alt="Patient Image" style="max-width: 100%; border-radius: 10px; margin-bottom: 20px;">
            <form method="post" action="{{ url_for('patient_detail', patient_id=patient_id) }}">
                <div class="form-group">
                    <label for="report">Report:</label>
                    <textarea name="report" id="report" rows="10" required>{{ patient.report }}</textarea>
                </div>
                <div class="form-group">
                    <button type="submit">Save Report</button>
                </div>
            </form>
            <a href="{{ url_for('patient_table') }}" class="back-link">Back to Patient List</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, patient=patient, patient_id=patient_id)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # هنا يمكنك إضافة الشيفرة لمعالجة البيانات مثل إرسال بريد إلكتروني أو حفظ البيانات
        flash('Your message has been sent successfully!')
        return redirect(url_for('contact'))

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            h2 {
                text-align: center;
                color: #0056b3;
            }
            .form-group {
                margin-bottom: 20px;
            }
            .form-group label {
                display: block;
                font-weight: bold;
                margin-bottom: 5px;
            }
            .form-group input, .form-group textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                resize: vertical;
            }
            .form-group button {
                background-color: #0056b3;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            .form-group button:hover {
                background-color: #004494;
            }
            .back-link {
                display: block;
                text-align: center;
                margin-top: 20px;
                text-decoration: none;
                color: #0056b3;
            }
            .back-link:hover {
                text-decoration: underline;
            }
            .alert {
                color: green;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Contact Us</h2>
            {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="alert">
                    {{ messages[0] }}
                </div>
            {% endif %}
            {% endwith %}
            <form method="post">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" rows="5" required></textarea>
                </div>
                <div class="form-group">
                    <button type="submit">Submit</button>
                </div>
            </form>
            <a href="{{ url_for('patient_table') }}" class="back-link">Back to Patient List</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
