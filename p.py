from flask import Flask, render_template_string, request, redirect, url_for, flash, session

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
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
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
        <a href="{{ url_for('add_patient') }}">Add New Patient</a>
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

                 <td>
                    <a href="{{ url_for('edit_patient', patient_id=patient_id) }}">Edit</a> |
                    <a href="{{ url_for('delete_patient', patient_id=patient_id) }}" onclick="return confirm('Are you sure you want to delete this patient?')">Delete</a>
                </td>

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

        <!-- Accordion Section -->
        <div class="container">
            <h2>Medical Information</h2>
            <div id="accordion">
                <div class="card">
                    <div class="card-header" id="headingOne">
                        <h5 class="mb-0">
                            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                General Medicine
                            </button>
                        </h5>
                    </div>
                    <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                        <div class="card-body">
                            <p>General medicine involves the diagnosis and treatment of various medical conditions and diseases. It covers a wide range of health issues and is the cornerstone of primary healthcare.</p>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header" id="headingTwo">
                        <h5 class="mb-0">
                            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                Pediatrics
                            </button>
                        </h5>
                    </div>
                    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                        <div class="card-body">
                            <p>Pediatrics focuses on the health and medical care of infants, children, and adolescents. Pediatricians specialize in diagnosing and treating childhood illnesses and disorders.</p>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header" id="headingThree">
                        <h5 class="mb-0">
                            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                Cardiology
                            </button>
                        </h5>
                    </div>
                    <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
                        <div class="card-body">
                            <p>Cardiology is the branch of medicine dealing with disorders of the heart and blood vessels. Cardiologists diagnose and treat conditions like heart disease, hypertension, and arrhythmias.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer class="footer">
            <div class="footer-content">
                <div class="footer-logo">
                    <img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
                </div>
                <div class="footer-links">
                    <h3>Links</h3>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Services</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-insurances">
                    <h3>Insurances</h3>
                    <ul>
                        <li><a href="#">Insurance A</a></li>
                        <li><a href="#">Insurance B</a></li>
                        <li><a href="#">Insurance C</a></li>
                    </ul>
                </div>
                <div class="footer-social">
                    <h3>Follow Us</h3>
                    <a href="#"><img src="{{ url_for('static', filename='images/2023_Facebook_icon.svg (1).png') }}" alt="Facebook"></a>
                    <a href="#"><img src="{{ url_for('static', filename='images/download (2).png') }}" alt="Twitter"></a>
                    <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1)..png') }}" alt="Instagram"></a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Your Company. All rights reserved. <a href="#">Privacy Policy</a></p>
            </div>
        </footer>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    </body>
    </html>
    '''

    return render_template_string(html, filtered_patients=filtered_patients)

@app.route('/patient/<patient_id>', methods=['GET', 'POST'])
def patient_detail(patient_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    patient = patients.get(patient_id)
    if not patient:
        flash('Patient not found!', 'error')
        return redirect(url_for('patient_table'))

    if request.method == 'POST':
        report = request.form.get('report', '')
        patient['report'] = report
        patient['report_saved'] = True
        flash('Report saved successfully!', 'success')
        return redirect(url_for('patient_table'))

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Patient Details</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-4">
            <h2>Patient Details</h2>
            <img src="{{ url_for('static', filename='images/' + patient.image) }}" alt="Patient Image" width="200">
            <p><strong>Name:</strong> {{ patient.name }}</p>
            <p><strong>Age:</strong> {{ patient.age }}</p>
            <p><strong>Checkpoint:</strong> {{ patient.checkpoint }}</p>
            <form method="post">
                <div class="form-group">
                    <label for="report">Report:</label>
                    <textarea class="form-control" id="report" name="report" rows="5">{{ patient.report }}</textarea>
                </div>
                <button type="submit" class="btn btn-primary">Save Report</button>
            </form>
            <a href="{{ url_for('patient_table') }}" class="btn btn-secondary mt-3">Back to Table</a>
        </div>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    </body>
    </html>
    '''
    return render_template_string(html, patient=patient)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('patient_table'))
        flash('Invalid username or password!', 'error')
    return '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-4">
            <h2>Login</h2>
            <form method="post">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" class="form-control" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
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

@app.route('/edit/<patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    patient = patients.get(patient_id)
    if not patient:
        return "Patient not found", 404

    if request.method == 'POST':
        patient['name'] = request.form['name']
        patient['age'] = request.form['age']
        patient['checkpoint'] = request.form['checkpoint']
        flash('Patient details updated successfully!')
        return redirect(url_for('patient_table'))

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Patient</title>
        <style>
            /* إضافة الأنماط المناسبة */
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Edit Patient - {{ patient.name }}</h2>
            <form method="post">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" value="{{ patient.name }}" required>
                </div>
                <div class="form-group">
                    <label for="age">Age:</label>
                    <input type="number" id="age" name="age" value="{{ patient.age }}" required>
                </div>
                <div class="form-group">
                    <label for="checkpoint">Check Point:</label>
                    <input type="text" id="checkpoint" name="checkpoint" value="{{ patient.checkpoint }}" required>
                </div>
                <div class="form-group">
                    <button type="submit">Save Changes</button>
                </div>
            </form>
            <a href="{{ url_for('patient_table') }}" class="back-link">Back to Patient List</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, patient=patient)


@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_id = str(max(int(id) for id in patients.keys()) + 1)
        patients[new_id] = {
            "name": request.form['name'],
            "age": request.form['age'],
            "checkpoint": request.form['checkpoint'],
            "image": request.form['image'],
            "report": "",
            "report_saved": False
        }
        flash('New patient added successfully!')
        return redirect(url_for('patient_table'))

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add Patient</title>
        <style>
            /* إضافة الأنماط المناسبة */
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Add New Patient</h2>
            <form method="post">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="age">Age:</label>
                    <input type="number" id="age" name="age" required>
                </div>
                <div class="form-group">
                    <label for="checkpoint">Check Point:</label>
                    <input type="text" id="checkpoint" name="checkpoint" required>
                </div>
                <div class="form-group">
                    <label for="image">Image Filename:</label>
                    <input type="text" id="image" name="image" required>
                </div>
                <div class="form-group">
                    <button type="submit">Add Patient</button>
                </div>
            </form>
            <a href="{{ url_for('patient_table') }}" class="back-link">Back to Patient List</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/delete/<patient_id>')
def delete_patient(patient_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    if patient_id in patients:
        del patients[patient_id]
        flash('Patient deleted successfully!')
    else:
        flash('Patient not found!')
    
    return redirect(url_for('patient_table'))



if __name__ == '__main__':
    app.run(debug=True)
