from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tusharpal_8865'
app.config['MYSQL_DB'] = 'student_registration'

mysql = MySQL(app)

@app.route('/')
def registration_form():
    return render_template('flex_project.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        DOB = request.form['DOB']
        blood_group = request.form['blood_group']
        address = request.form['address']
        department = request.form['department']
        course = request.form['course']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, father_name, mother_name, phone_number, email, DOB, blood_group, address, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (name, father_name, mother_name, phone_number,email, DOB, blood_group, address, department, course, password))
        mysql.connection.commit()
        cur.close()

        return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
    