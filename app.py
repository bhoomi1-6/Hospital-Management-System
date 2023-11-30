# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)


app.secret_key = 'svfdbhfgtjr'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxx'
app.config['MYSQL_DB'] = 'hms3'

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM admin WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['username'] = account['username']
			session['password'] = account['password']
			msg = 'Logged in successfully !'
			return render_template('admin_index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/dlogin', methods =['GET', 'POST'])
def dlogin():
	msg = ''
	if request.method == 'POST' and 'ID' in request.form and 'password' in request.form:
		ID = request.form['ID']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM doctor WHERE doctor_id = % s AND password = % s', (ID, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['ID'] = account['doctor_id']
			session['password'] = account['password']
			msg = 'Logged in successfully !'
			return render_template('doctor_index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)



@app.route('/plogin', methods =['GET', 'POST'])
def plogin():
      msg = ''
      if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM patient WHERE username = % s AND password = % s', (username, password, ))
            account = cursor.fetchone()
            if account:
                  session['loggedin'] = True
                  session['username'] = account['username']
                  session['password'] = account['password']
                  session['patient_ID'] = account["patient_ID"]
                  msg = 'Logged in successfully !'
                  return render_template('patient_index.html',msg = msg)	
            else:
                  msg = 'Incorrect username / password !'
      
      return render_template('login.html', msg = msg)



@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	#session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))


@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		#email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM admin WHERE username = % s', (username,))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO admin (username,password) VALUES (% s, % s)', (username, password))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)




app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:xxx@localhost/hms3'  # Replace with your MySQL credentials
db = SQLAlchemy(app)




class Admin(db.Model):
      __tablename__='Admin'
      username = db.Column(db.Integer, primary_key=True, nullable = False)
      password = db.Column(db.String(100), nullable=False)

#Define Doctor and Patient models
class Doctor(db.Model):
      __tablename__='doctor'
      doctor_id = db.Column(db.Integer, primary_key=True, nullable = False)
      doctor_name = db.Column(db.String(100), nullable=False)
      username = db.Column(db.String(100))
      specialisation = db.Column(db.String(100), nullable=False)
      password = db.Column(db.String(100), nullable=False)
      consultFee = db.Column(db.Integer, nullable=False)


class Patient(db.Model):
      __tablename__='Patient'
      patient_ID = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(100), primary_key=True)
      patient_Name = db.Column(db.String(100), nullable=False)
      password = db.Column(db.String(100), nullable=False)
      apt_Number = db.Column(db.Integer,db.ForeignKey('appointment.apt_Number'))
      bill_id = db.Column(db.Integer, db.ForeignKey('Bill.bill_id'))
      bedID = db.Column(db.Integer, db.ForeignKey('Bed.bedID'))


class AppointmentStatus(db.Model):
    __tablename__ = 'appointment_status'

    status = db.Column(db.String(15), primary_key=True, nullable=False)
    apt_Number = db.Column(db.Integer, db.ForeignKey('appointment.apt_Number'), primary_key=True, nullable=False)
    
    # Define the relationship with the Appointment model
    appointment = db.relationship('Appointment', backref='appointment_status')

    def __init__(self, status, apt_Number):
        self.status = status
        self.apt_Number = apt_Number

class Bill(db.Model):
    __tablename__='Bill'
    bill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_ID = db.Column(db.Integer, db.ForeignKey('Patient.patient_ID'))
    Bill_Amount = db.Column(db.Float, nullable=False)
    username = db.Column(db.String(15), db.ForeignKey('Admin.username'))


class Appointment(db.Model):
    __tablename__ = 'appointment'
    apt_Number = db.Column(db.Integer, primary_key=True, autoincrement = True)
    date = db.Column(db.Date, nullable=False)
    Time = db.Column(db.String(15), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    patient_ID = db.Column(db.Integer, db.ForeignKey('Patient.patient_ID'))
    doctor = db.relationship('Doctor', backref='Appointment')
    def __init__(self, date,Time,doctor_id, apt_Number,patient_ID):
        self.date = date
        self.Time=Time
        self.doctor_id=doctor_id
        self.apt_Number = apt_Number
        self.patient_ID = patient_ID


class Bed(db.Model):
    __tablename__='Bed'
    bedID = db.Column(db.Integer, primary_key=True, autoincrement=True)



class Bed_BedType(db.Model):
    __tablename__ = 'Bed_BedType'
    BedType = db.Column(db.String(20), primary_key=True, nullable=False)
    bedID = db.Column(db.Integer, db.ForeignKey('Bed.bedID'), primary_key=True, nullable=False)


class Bed_BedCost(db.Model):
    __tablename__ = 'Bed_BedCost'
    BedCost = db.Column(db.Integer, primary_key=True, nullable=False)
    bedID = db.Column(db.Integer, db.ForeignKey('Bed.bedID'), primary_key=True, nullable=False)


def __init__(self, doctor_id, date, Time,patient_ID):
        self.doctor_id = doctor_id
        self.date = date
        self.Time = Time
        self.patient_ID = patient_ID
        
		
class Prescription(db.Model):
            __tablename__ = 'Prescription'
            presc_ID = db.Column(db.Integer, primary_key=True)
            diagnosis = db.Column(db.String(20), nullable=False)
            description = db.Column(db.String(20), nullable=False)
            doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
            patient_ID = db.Column(db.Integer, db.ForeignKey('Patient.patient_ID'))
            admit = db.Column(db.Enum('yes', 'no'), default='no', nullable=False)
        

class Prescription_medicines(db.Model):
    __tablename__ = 'Prescription_medicines'
    medicines = db.Column(db.String(20), nullable=False)
    presc_ID = db.Column(db.Integer, db.ForeignKey('Prescription.presc_ID'), nullable=False, primary_key=True)
    



# Routes

# Add a doctor
@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        new_doctor = Doctor(doctor_name=request.form['name'], doctor_id = request.form['ID'],password = request.form['pass'],specialisation = request.form['spl'],consultFee = request.form['fee'],username=request.form['username'])
        db.session.add(new_doctor)
        db.session.commit()
        return redirect(url_for('admin_index'))
    return render_template('add_doctor.html')



# Route to render the form
@app.route('/update_doctor_form', methods=['GET'])
def update_doctor_form():
    return render_template('update_doctor.html')

# Route to handle the form submission and update the doctor's name
@app.route('/update_doctor', methods=['GET','POST'])
def update_doctor():
    doctor_id = request.form['doctor_id']
    new_name = request.form['new_name']
    # Retrieve the doctor from the database
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        # Update the doctor's name
        doctor.doctor_name = new_name

        # Commit the changes to the database
        db.session.commit()
        return "Doctor name updated successfully!"
    else:
        return "Doctor not found"
	


@app.route('/delete_doctor/<int:doctor_id>', methods=['GET','POST'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return redirect(url_for('admin_index'))
    else:
        return "Doctor not found"

	




@app.route('/admin_index')
def admin_index():
    #patients = Patient.query.all()
    doctors = Doctor.query.all()
    return render_template('admin_index.html', doctors=doctors)

@app.route('/d_index')
def d_index():
    return render_template('doctor_index.html' )




@app.route('/p_index')
def p_index():
    patients = Patient.query.all()
    doctors = Doctor.query.all()
    patient_ID = session['patient_ID']
    prescription = Prescription.query.filter_by(patient_ID=patient_ID).all()
    
    return render_template('patient_index.html', doctors=doctors,prescription=prescription,patients=patients)


@app.route('/p_index_pres')
def p_index_pres():
 
 patient_ID = session['patient_ID']
 prescriptions = Prescription.query.filter_by(patient_ID=patient_ID).all()
 prescription_medicines = {}
 for prescription in prescriptions:
        medicines = Prescription_medicines.query.filter_by(presc_ID=prescription.presc_ID).all()
        prescription_medicines[prescription.presc_ID] = medicines
 #prescription_medicines= Prescription_medicines.query.filter_by(presc_ID = Prescription.presc_ID).all()
 return render_template('patient_index.html',prescriptions=prescriptions,prescription_medicines=prescription_medicines)

      

@app.route('/patient_info', methods = ['GET','POST'])
def patient_info():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and'name' in request.form and 'password' in request.form:
		username = request.form['username']
		pname = request.form['name']
		password = request.form['password']
		#email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM patient WHERE username = % s', (username,))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not pname or not password:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO patient (username,patient_Name,password) VALUES (% s, % s,% s)', (username,pname,password))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fillll !'
	return render_template('patient_register.html', msg = msg)




from datetime import datetime



@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    msg = ''
    if request.method == 'POST' and 'doctor_id' in request.form and 'date' in request.form and 'time' in request.form:
        doctor_id = request.form['doctor_id']
        date_str = request.form['date']
        time_str = request.form['time']
        patient_ID = session['patient_ID']

        # Convert date and time strings to datetime objects
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time = datetime.strptime(time_str, '%H:%M').time()
        except ValueError:
            msg = 'Invalid date or time format'
            return render_template('book_appointment.html', msg=msg)

        # Check if the appointment slot is available
        existing_appointment = Appointment.query.filter_by(doctor_id=doctor_id, date=date, Time=time,patient_ID = patient_ID).first()
        if existing_appointment:
            msg = 'Appointment slot not available. Please choose another time.'
        else:
            # Create a new appointment
            new_appointment = Appointment(doctor_id=doctor_id, date=date, Time=time,patient_ID=patient_ID,apt_Number=None)
            db.session.add(new_appointment)
            db.session.commit()
            msg = 'Appointment booked successfully!'
            
			# Update the Patient table with the new appointment number
            patient_id = session.get('patient_ID')  # Assuming you store patient_ID in the session
            patient = Patient.query.filter_by(patient_ID=patient_id).first()

            if patient:
                patient.apt_Number = new_appointment.apt_Number
                db.session.commit()
    else:
        msg = 'Please fill out the form.'

    # Fetch doctors for dropdown
    doctors = Doctor.query.all()

    return render_template('book_appointment.html', msg=msg, doctors=doctors)




@app.route('/manage_appointments', methods=['GET'])
def manage_appointments():
      doctor_username  = session["ID"]
      appointments = Appointment.query.filter_by(doctor_id =doctor_username).all()
      appointment_status = AppointmentStatus.query.all()
      appointment_data=[] 
      for apt in appointments:
            status = next((s for s in appointment_status if s.apt_Number == apt.apt_Number), None)
            patient = Patient.query.filter_by(apt_Number=apt.apt_Number).first()
            appointment_data.append((apt, status,patient))
      return render_template('manage_appointments.html', appointments=appointment_data)



@app.route('/confirm_cancel_appointment/<int:apt_number>/<string:status>', methods=['GET'])
def confirm_cancel_appointment(apt_number, status):
    # Fetch the appointment and its status
    appointment = Appointment.query.get(apt_number)
    appointment_status = AppointmentStatus.query.filter_by(apt_Number=apt_number).first()
    doctor_username = session["ID"]
    # If appointment_status is None, create a new one
    if appointment_status is None:
        appointment_status = AppointmentStatus(apt_Number=apt_number, status=status)
        db.session.add(appointment_status)
        
    if appointment_status is not None:
          appointment_status.status = status


    # Update the status
    #appointment_status.status = status
    # Update the Patient tuple with the apt_Number if the appointment is confirmed)
    #if status == 'Confirm':

    patient = Patient.query.filter_by(apt_Number=apt_number).first()
    if patient:
          patient.apt_Number = apt_number
          db.session.commit()
    

    # Commit the changes to the database
    

    return redirect(url_for('manage_appointments'))


@app.route('/my_appointment_details', methods=['GET'])
def my_appointment_details():
    # Retrieve the current patient from the database
    current_patient = Patient.query.filter_by(username=session['username']).first()

    if not current_patient:
        return "patient hasnt booked appointment"

    # Retrieve the appointment details for the current patient
    appointment = Appointment.query.filter_by(apt_Number=current_patient.apt_Number).first()

    if not appointment:
        return "patient hasnt booked appointment"

    # Retrieve the appointment status for the current appointment
    appointment_status = AppointmentStatus.query.filter_by(apt_Number=appointment.apt_Number).first()
    if appointment_status is None:
          return "ON HOLD"

    return render_template('my_appointment_details.html', patient=current_patient, appointment=appointment, status=appointment_status.status)



# Route for the "write prescription" form
@app.route('/write_prescription', methods=['GET', 'POST'])
def write_prescription():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        presc_ID = request.form['presc_ID']
        patient_ID = request.form['patient_ID']
        diagnosis = request.form['diagnosis']
        description = request.form['description']
        medicines = request.form['medicines']
        admit = request.form['admit']

        # Assuming you have the doctor_id available, replace 1 with the actual doctor_id
        
        # Create a new Prescription object
        prescription = Prescription(presc_ID=presc_ID,diagnosis=diagnosis,description=description,patient_ID=patient_ID,doctor_id=doctor_id,admit=admit)
        #medicines_list = medicines.split(',')
        prescription_medicines=[]
        db.session.add(prescription)
        db.session.commit()
        prescription_med = Prescription_medicines(medicines=medicines, presc_ID=prescription.presc_ID)
        db.session.add(prescription_med)
        db.session.commit()
        # Add the new prescription to the database


        return redirect(url_for('d_index'))  # Redirect to doctor's index page

    # Render the prescription form
    return render_template('write_prescription.html')



@app.route('/bed_allocation/<int:presc_ID>', methods=['GET', 'POST'])
def bed_allocation(presc_ID):
    prescription = Prescription.query.get(presc_ID)
    prescriptions = Prescription.query.all()
    BEDTYPES = Bed_BedType.query.all()
    allocated_bed_info = None  # Initialize with None or an appropriate default value
    if prescription is None or prescription.admit != 'yes':
        return "patient is an out-patient"

    if request.method == 'POST':
        # Process bed allocation form data
        bed_type = request.form['bed_type']
        if bed_type not in ['Single', 'Double']:
              return "Invalid bed type selected"
        for bed in Bed.query.all():
            bed_type_info = Bed_BedType.query.filter_by(BedType=bed_type, bedID=bed.bedID).first()
        # bed_info = Bed.query.first()
        # bed_type_info = Bed_BedType.query.filter_by(BedType=bed_type,bedID=bed_info.bedID).first()
        
        if bed_type_info is None:
              new_bed_type = Bed_BedType(BedType=bed_type,bedID = bed.bedID)
              db.session.add(new_bed_type)
              db.session.commit()
              bed_type_info = Bed_BedType.query.filter_by(BedType=bed_type).first()
        if bed_type == 'Single':
              bed_cost = 800
        elif bed_type == 'Double':
              bed_cost = 1600
        else:
              return "Invalid bed type selected"
   

        
        patient = Patient.query.filter_by(patient_ID=prescription.patient_ID).first()
        patient.bedID = bed_type_info.bedID
        if patient:
              patient.bedID = bed_type_info.bedID
        else:
              return "Patient record not found"
        
        bed_cost_info = Bed_BedCost.query.filter_by(bedID=bed_type_info.bedID).first()

        if bed_cost_info is None:
            bed_cost_info = Bed_BedCost(BedCost=bed_cost, bedID=bed_type_info.bedID)
            db.session.add(bed_cost_info)
        else:
            bed_cost_info.BedCost = bed_cost
            
        db.session.commit()
        allocated_bed_info = {
            'BedID': bed_type_info.bedID,
            'BedType': bed_type_info.BedType,
            'BedCost': bed_cost
        }
               

    # Fetch bed types for the dropdown in the form
    bed_types = [row.BedType for row in Bed_BedType.query.all()]

    return render_template('bed_allocation_form.html', prescription=prescription,prescriptions=prescriptions, bed_types=bed_types,BEDTYPES=BEDTYPES,allocated_bed_info=allocated_bed_info)



def calculate_total_bill(bed_cost, consult_fee):
    if consult_fee is None:
          return 0
    return bed_cost + consult_fee


# @app.route('/generate_bill', methods=['GET', 'POST'])
# def generate_bill():
#     if request.method == 'POST':
#         patient_ID = request.form['patient_ID']
#         # # Fetch the patient based on the entered patient_id
#         patient = Patient.query.filter_by(patient_ID=patient_ID).first()

#         if patient:
#             # Fetch the bed cost for the patient
#             bed_cost_info = Bed_BedCost.query.filter_by(bedID=patient.bedID).first()

#             # Fetch the doctor's consultation fee
#             doctor = Doctor.query.filter_by(doctor_id=patient.apt.appointment.doctor_id).first()

#             # Calculate the total bill amount
#             total_bill_amount = calculate_total_bill(bed_cost_info.BedCost, doctor.consultFee)

#             # Create a new bill
#             bill = Bill(Bill_Amount=total_bill_amount,patient_ID= session[patient_ID])

#             # Add the new bill to the database
#             db.session.add(bill)
#             db.session.commit()

#             # Update the patient's bill_id
#             patient.bill_id = bill.bill_id
#             db.session.commit()

#             return render_template('bill_generated.html', patient=patient, bill=bill)

#         else:
#             return "Patient not found. Please enter a valid patient ID."

#     return render_template('generate_bill.html')

from sqlalchemy.orm import aliased
from sqlalchemy.sql import func


# @app.route('/generate_bill', methods=['GET','POST'])
# def generate_bill():
#     if request.method == 'POST':
#         patient_ID = request.form['patient_ID']

#         # Fetch the patient based on the entered patient_id
#         patient = Patient.query.filter_by(patient_ID=patient_ID).first()

#         if patient:
#             # Join tables to fetch appointment and doctor information
#            appointment_info = db.session.query(Appointment, Doctor).\
#                 join(Doctor, Appointment.doctor_id == Doctor.doctor_id).\
#                 join(Patient, Appointment.apt_Number == Patient.apt_Number).\
#                 filter(Patient.patient_ID == patient_ID).first()
#            if appointment_info:
#                 appointment, doctor = appointment_info

#                 # Fetch the bed cost for the patient
#                 bed_cost_info = Bed_BedCost.query.filter_by(bedID=patient.bedID).first()
#                 bed_cost = bed_cost_info.BedCost if bed_cost_info else 0
#                 # Calculate the total bill amount
#                 total_bill_amount = calculate_total_bill(bed_cost, doctor.consultFee)

#                 # Create a new bill
#                 bill = Bill(patient_ID=patient_ID, Bill_Amount=total_bill_amount, username = session['username'])

#                 # Add the new bill to the database
#                 db.session.add(bill)
#                 db.session.commit()

#                 # Update the patient's bill_id
#                 patient.bill_id = bill.bill_id
#                 db.session.commit()

#                 return render_template('bill_generated.html', patient=patient, bill=bill)
#            else:
#                 return "Appointment not found for the patient."
#         else:
#            return "Patient not found. Please enter a valid patient ID."
#     return render_template('generate_bill.html')



@app.route('/generate_bill', methods=['GET', 'POST'])
def generate_bill():
    if request.method == 'POST':
        patient_ID = request.form["patient_ID"]
        # Fetch the patient based on the entered patient_id
        patient = Patient.query.filter_by(patient_ID=patient_ID).first()

        if patient:

            # Calculate the total consultation fee for all appointments
            total_consult_fee = db.session.query(func.sum(Doctor.consultFee)).\
                join(Appointment, Appointment.doctor_id == Doctor.doctor_id).\
                filter(Appointment.patient_ID == patient_ID).scalar()

            # Fetch the bed cost for the patient
            bed_cost_info = Bed_BedCost.query.filter_by(bedID=patient.bedID).first()
            bed_cost = bed_cost_info.BedCost if bed_cost_info else 0
            # Calculate the total bill amount
            total_bill_amount = calculate_total_bill(bed_cost, total_consult_fee)

            # Create a new bill
            bill = Bill(Bill_Amount=total_bill_amount, patient_ID=patient_ID,username = session['username'])

            # Add the new bill to the database
            db.session.add(bill)
            db.session.commit()

            # Update the patient's bill_id
            patient.bill_id = bill.bill_id
            db.session.commit()

            return render_template('bill_generated.html', patient=patient, bill=bill)

        else:
            return "Patient not found / Patient's Appointment has got cancelled"

    return render_template('generate_bill.html')


@app.route('/get_total_bill_revenue', methods=['GET'])
def get_total_bill_revenue():
    cursor = mysql.connection.cursor()
    cursor.execute('CALL calculate_total_bill_revenue()')
    total_revenue = cursor.fetchone()[0]
    cursor.close()
    return render_template('total_revenue.html',total_revenue=total_revenue)


@app.route('/pop_doc', methods=['GET'])
def pop_doc():
    cursor = mysql.connection.cursor()
    cursor.execute('CALL calc_most_popular_doctor()')
    pop_doc = cursor.fetchone()
    cursor.close()
    return render_template('pop_doc.html',pop_doc=pop_doc)


@app.route('/admitted', methods=['GET'])
def admitted():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) AS total_admitted FROM Patient WHERE BedID IS NOT NULL')
    ap = cursor.fetchone()[0]
    cursor.close()
    return render_template('admitted.html',ap=ap)


# @app.route('/pdt', methods=['GET'])
# def pdt():
#     cursor = mysql.connection.cursor()
#     cursor.execute(' SELECT p.patient_ID AS patient_id,p.patient_name AS patient_name,a.date AS appointment_date,a.time AS appointment_time FROM Patient p LEFT JOIN Appointment a ON p.patient_ID = a.patient_ID')
#     pdt = cursor.fetchone()[0]
#     cursor.close()
#     return render_template('pdt.html',pdt=pdt)

@app.route('/pdt', methods=['GET'])
def pdt():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT p.patient_ID AS patient_id, p.patient_name AS patient_name, a.date AS appointment_date, a.time AS appointment_time FROM Patient p LEFT JOIN Appointment a ON p.patient_ID = a.patient_ID')
    pdt = cursor.fetchall()
    cursor.close()
    return render_template('pdt.html', pdt=pdt)

@app.route('/bed_info', methods=['GET'])
def bed_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT bbt.BedID AS bed_id, bbt.BedType AS bed_type, bbc.BedCost AS bed_cost, p.patient_ID AS patient_id FROM Bed_BedType bbt JOIN Bed_BedCost bbc ON bbt.BedID = bbc.BedID JOIN Patient p ON bbc.BedID = p.BedID WHERE p.BedID IS NOT NULL')
    bed_info = cursor.fetchall()
    cursor.close()
    return render_template('bed_info.html',bed_info=bed_info)



if __name__ == '__main__':
	app.run(debug=True)

















