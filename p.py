from flask import Flask, render_template_string, request, redirect, url_for,flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
patients = {
    "159": {"name": "John Doe", "age": 30, "checkpoint": "Checkup", "image": "download (3).jpeg", "report": "", "report_saved": False},
    "160": {"name": "Jane Smith", "age": 25, "checkpoint": "Follow-up", "image": "download.jpeg", "report": "", "report_saved": False},
    "161": {"name": "Alice Brown", "age": 40, "checkpoint": "Diagnosis", "image": "download (1).jpeg", "report": "", "report_saved": False},
    "162": {"name": "Mena Magdy", "age": 22, "checkpoint": "Diseases", "image": "4.jpeg", "report": "", "report_saved": False},
    "163": {"name": "Youssef Rafat", "age": 23, "checkpoint": "Salts", "image": "5.jpeg", "report": "", "report_saved": False},
    "165": {"name": "Ahmed Ashraf", "age": 40, "checkpoint": "Sugar", "image": "images.jpeg", "report": "", "report_saved": False}
}



@app.route('/', methods=['GET', 'POST'])
def patient_table():
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
        </style>
    </head>
    <body>
        <div class="navbar">
            <a href="{{ url_for('patient_table') }}">Home</a>
            <a href="{{ url_for('patient_table') }}">Patients</a>
            <a href="{{ url_for('contact') }}">Contact</a>
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
       <div class="footer">
    <div class="footer-content">
        
        <div class="footer-links">
            <ul>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Annual Checkup</a></li>
                <li><a href="#">Blog</a></li>
                <li><a href="#">Careers</a></li>
                <li><a href="#">Get a Diagnosis</a></li>
                <li><a href="#">How it Works</a></li>
                <li><a href="#">Privacy Policy</a></li>
            </ul>
        </div>
        <div class="footer-insurances">
            <h3>Top Insurances</h3>
            <ul>
                <li><a href="#">Aetna</a></li>
                <li><a href="#">Health Plan</a></li>
                <li><a href="#">Blue Shield</a></li>
                <li><a href="#">Health Net</a></li>
                <li><a href="#">Health Smarth</a></li>
                <li><a href="#">View More</a></li>
            </ul>
        </div>
        <div class="footer-social">
            <h3>Follow Us</h3>
            <a href="#"><img src="{{ url_for('static', filename='images/2023_Facebook_icon.svg (1).png') }}" alt="Facebook"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (2).png') }}" alt="Twitter"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1).png') }}" alt="LinkedIn"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1)..png') }}" alt="Instagram"></a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; All rights reserved by Medical 2020</p>
        <a href="#">Privacy Policy</a> | <a href="#">Terms & Conditions</a>
    </div>
</div>
    </body>
    </html>
    '''
    return render_template_string(html, filtered_patients=filtered_patients)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        phone = request.form['phone']
        address = request.form['address']
        description = request.form['description']


        flash('Your message has been sent!')
        return redirect(url_for('contact'))

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Information</title>
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
            .contact-form {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: 20px auto;
            }
            .contact-form h2 {
                text-align: center;
                color: #0056b3;
                margin-bottom: 20px;
            }
            .contact-form label {
                font-size: 16px;
                margin-bottom: 5px;
                display: block;
            }
            .contact-form input, .contact-form textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 5px;
                box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
            }
            .contact-form button {
                background-color: #0056b3;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                display: block;
                width: 100%;
                margin-top: 10px;
            }
            .contact-form button:hover {
                background-color: #004494;
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
        </style>
    </head>
    <body>
        <div class="navbar">
            <a href="{{ url_for('patient_table') }}">Home</a>
            <a href="{{ url_for('patient_table') }}">Patients</a>
            <a href="{{ url_for('contact') }}">Contact</a>
        </div>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="alert" style="text-align: center; color: green; font-weight: bold; margin-bottom: 20px;">
                {{ messages[0] }}
            </div>
        {% endif %}
        {% endwith %}
        <div class="contact-form">
            <h2>Contact Us</h2>
            <form method="post">
                <label for="phone">Phone Number</label>
                <input type="text" id="phone" name="phone" required>

                <label for="address">Address</label>
                <input type="text" id="address" name="address" required>

                <label for="description">Description of Problem</label>
                <textarea id="description" name="description" rows="5" required></textarea>

                <button type="submit">Send Message</button>
            </form>
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
                <li><a href="#">How it Works</a></li>
                <li><a href="#">Privacy Policy</a></li>
            </ul>
        </div>
        <div class="footer-insurances">
            <h3>Top Insurances</h3>
            <ul>
                <li><a href="#">Aetna</a></li>
                <li><a href="#">Health Plan</a></li>
                <li><a href="#">Blue Shield</a></li>
                <li><a href="#">Health Net</a></li>
                <li><a href="#">Health Smarth</a></li>
                <li><a href="#">View More</a></li>
            </ul>
        </div>
        <div class="footer-social">
            <h3>Follow Us</h3>
            <a href="#"><img src="{{ url_for('static', filename='images/2023_Facebook_icon.svg (1).png') }}" alt="Facebook"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (2).png') }}" alt="Twitter"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1).png') }}" alt="LinkedIn"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1)..png') }}" alt="Instagram"></a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; All rights reserved by Medical 2020</p>
        <a href="#">Privacy Policy</a> | <a href="#">Terms & Conditions</a>
    </div>
</div>    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/patient/<patient_id>', methods=['GET', 'POST'])
def patient_detail(patient_id):
    patient = patients.get(patient_id, None)

    if patient is None:
        return "patient not found", 404

    if request.method == 'POST':
        patient['report'] = request.form['report']
        patient['report_saved'] = True
        return redirect(url_for('patient_detail', patient_id=patient_id))

    html = '''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تفاصيل {{ patient.name }}</title>
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
            img {
                display: block;
                margin: 0 auto 20px auto;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            form {
                text-align: center;
            }
            textarea {
                width: 80%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 5px;
                box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
            }
            button {
                background-color: #0056b3;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #004494;
            }
            label {
                font-size: 18px;
                margin-top: 20px;
                display: block;
                text-align: center;
            }
            input[type="checkbox"] {
                transform: scale(1.5);
                margin-right: 10px;
            } .report-box {
                width: 80%;
                margin: 20px auto;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .back-button {
                display: block;
                width: 80%;
                margin: 20px auto;
                text-align: center;
            }
            .back-button a {
                text-decoration: none;
                background-color: #0056b3;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }
            .back-button a:hover {
                background-color: #004494;
            }
    .footer {
        background-color:#0056b3;
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
        display:inline;
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
        </style>
    </head>
    <body>
        <div class="navbar">
            <a href="{{ url_for('patient_table') }}">Home</a>
            <a href="{{ url_for('patient_table') }}">Patients</a>
            <a href="#">Contact</a>
        </div>
        <h1>Details {{ patient.name }}</h1>
        <img src="{{ url_for('static', filename='images/' + patient.image) }}" alt="Patient Image" width="400"><br>
        <form method="post">
            <label>Report:</label><br>
            <textarea name="report" rows="5" cols="40">{{ patient.report }}</textarea><br>
            <button type="submit">Save</button>
        </form>
        <br>
        {% if patient.report %}
        <div class="report-box">
            <h3>Saved Report:</h3>
            <p>{{ patient.report }}</p>
        </div>
        {% endif %}
        <div class="back-button">
            <a href="{{ url_for('patient_table') }}">Back</a>
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
                <li><a href="#">How it Works</a></li>
                <li><a href="#">Privacy Policy</a></li>
            </ul>
        </div>
        <div class="footer-insurances">
            <h3>Top Insurances</h3>
            <ul>
                <li><a href="#">Aetna</a></li>
                <li><a href="#">Health Plan</a></li>
                <li><a href="#">Blue Shield</a></li>
                <li><a href="#">Health Net</a></li>
                <li><a href="#">Health Smarth</a></li>
                <li><a href="#">View More</a></li>
            </ul>
        </div>
        <div class="footer-social">
            <h3>Follow Us</h3>
            <a href="#"><img src="{{ url_for('static', filename='images/2023_Facebook_icon.svg (1).png') }}" alt="Facebook"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (2).png') }}" alt="Twitter"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1).png') }}" alt="LinkedIn"></a>
            <a href="#"><img src="{{ url_for('static', filename='images/download (1) (1)..png') }}" alt="Instagram"></a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; All rights reserved by Medical 2020</p>
        <a href="#">Privacy Policy</a> | <a href="#">Terms & Conditions</a>
    </div>
</div>
      
    </body>
    </html>
    '''
    return render_template_string(html, patient=patient)

if __name__ == '__main__':
    app.run(debug=True)
