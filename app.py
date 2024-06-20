
from flask import Flask, render_template, request, redirect, url_for, flash

import dbConnect

app = Flask(__name__)
app.secret_key = 'supersecretkey'  
db_config = dbConnect.read_db_config()
dbConnect.execute_sql(db_config,"SELECT * from studentmaster") 
Packagess = []
clients = []
events = []
bookings = []
payments = []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_Packages', methods=['POST'])
def add_Packages():
    Packages_name = request.form['PackagesName']
    Low_Range = request.form['Low_Range']
    High_Range = request.form['High_Range']
    return redirect(url_for('home'))

@app.route('/update_Packages', methods=['POST'])
def update_Packages():
    Packages_name = request.form['PackagesName']
    Low_Range = request.form['Low_Range']
    High_Range = request.form['High_Range']
    return redirect(url_for('home'))

@app.route('/delete_Packages', methods=['POST'])
def delete_Packages():
    Packages_name = request.form['PackagesName']
    return redirect(url_for('home'))

@app.route('/view_Packages', methods=['POST'])
def view_Packages():
    Packages_name = request.form['PackagesName']
    return redirect(url_for('home'))

# Client Management Routes
@app.route('/add_client', methods=['POST'])
def add_client():
    client_id=str(request.form["clientId"])
    client_name = request.form['clientName']
    client_email = request.form['clientEmail']
    client_phone =str( request.form['clientPhone'])
    clients.append({'name': client_name, 'email': client_email, 'phone': client_phone})
    flash('Client added successfully!')
    query="INSERT INTO d_clients(client_number,first_name,last_name,phone,email) VALUES( "+client_id+",'"+client_name+"','"+client_name+"',"+client_phone+",'"+client_email+"')"
    print(query)
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    
    return redirect(url_for('home'))

@app.route('/update_client', methods=['POST'])
def update_client():
    if 1==1:
        client_id = str(request.form['clientId'])
        name =request.form['clientName'],
        email= request.form['clientEmail'],
        phone= str(request.form['clientPhone'])
        print(client_id,name,phone,email)
        query="UPDATE d_clients SET first_name = '"+name[0]+"', phone= "+phone+", email = '"+email[0]+"' WHERE client_number = "+client_id
        print(query)
        db_config = dbConnect.read_db_config()
        result=dbConnect.execute_sql(db_config,query)
        print("done")
        flash("NOT UPDATED")
        print("except")
    return redirect(url_for('home'))

@app.route('/delete_client', methods=['POST'])
def delete_client():
    print("in")
    client_id = str(request.form['clientId'])
    if 1==1:
        print("inin")
        query="DELETE FROM d_clients WHERE client_number = "+client_id
        print("ininin")
        db_config = dbConnect.read_db_config()
        print("inininin")
        result=dbConnect.execute_sql(db_config,query)
        print("done")
        flash('Client deleted successfully!')
    else:
        flash('Client not found!')
    return redirect(url_for('home'))

@app.route('/view_client', methods=['POST'])
def view_client():
    client_id = str(request.form['clientId'])
    query="select * from d_clients where client_number="+client_id
    db_config = dbConnect.read_db_config()
    print("inininin")
    result=dbConnect.execute_sql(db_config,query)
    print(result)
    if result==[]:
        data = {
        "name": "",
        "phone": "", 
        "id": "",
        "email": ""
    }
        return render_template('view.html', data=data)
    id, first_name, last_name, phone, email = result[0]
    data = {
    "name": f"{first_name} {last_name}",
    "phone": phone,
    "id": str(id),
    "email": email
}
    return render_template('view.html', data=data)

# Event Management Routes
@app.route('/create_event', methods=['POST'])
def create_event():
    event_id = str(request.form['eventId'])
    event_name = request.form['eventName']
    event_date = str(request.form['eventDate'])
    event_desc = request.form['eventLocation']
    event_cost = str(request.form['assignedDj'])
    venue=str(request.form['eventVenue'])
    PACKAGE_CODE=str(request.form['PACKAGE_CODE'])
    THEME_CODE=str(request.form['THEME_CODE'])
    CLIENT_NUMBER=str(request.form['CLIENT_NUMBER'])
    query="INSERT INTO d_clients(client_number,first_name,last_name,phone,email) VALUES( "+event_id+",'"+event_name+"','"+event_date+"',"+event_desc+",'"+event_cost+"')"
    print(query)
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    flash('Event created successfully!')
    return redirect(url_for('home'))

@app.route('/update_event', methods=['POST'])
def update_event():
    event_id = str(request.form['eventId'])
    event_name = request.form['eventName']
    event_date = str(request.form['eventDate'])
    event_desc = request.form['eventLocation']
    event_cost = str(request.form['assignedDj'])
    venue=str(request.form['eventVenue'])
    PACKAGE_CODE=str(request.form['PACKAGE_CODE'])
    THEME_CODE=str(request.form['THEME_CODE'])
    CLIENT_NUMBER=str(request.form['CLIENT_NUMBER'])
    return redirect(url_for('home'))

@app.route('/cancel_event', methods=['POST'])
def cancel_event():
    event_id = str(request.form['eventId'])
    return redirect(url_for('home'))

@app.route('/view_event', methods=['POST'])
def view_event():
    event_id = str(request.form['eventId'])
    return redirect(url_for('home'))

# Booking Management Routes
@app.route('/new_booking', methods=['POST'])
def new_booking():
    Theme_desc = request.form['bookingClient']
    Theme_id = request.form['bookingId']
    flash('Booking created successfully!')
    return redirect(url_for('home'))

@app.route('/update_booking', methods=['POST'])
def update_booking():
    Theme_desc = request.form['bookingClient']
    Theme_id = request.form['bookingId']
    return redirect(url_for('home'))

@app.route('/cancel_booking', methods=['POST'])
def cancel_booking():
    Theme_id = request.form['bookingId']
    return redirect(url_for('home'))

@app.route('/view_booking', methods=['POST'])
def view_booking():
    Theme_id = request.form['bookingId']
    return redirect(url_for('home'))

# Payment Management Routes
@app.route('/add_payment', methods=['POST'])
def add_payment():
    payment_client = request.form['paymentClient']
    payment_amount = request.form['paymentAmount']
    payment_date = request.form['paymentDate']
    payments.append({'client': payment_client, 'amount': payment_amount, 'date': payment_date})
    flash('Payment added successfully!')
    return redirect(url_for('home'))

@app.route('/update_payment', methods=['POST'])
def update_payment():
    payment_id = int(request.form['paymentId'])
    if payment_id < len(payments):
        payments[payment_id] = {
            'client': request.form['paymentClient'],
            'amount': request.form['paymentAmount'],
            'date': request.form['paymentDate']
        }
        flash('Payment updated successfully!')
    else:
        flash('Payment not found!')
    return redirect(url_for('home'))

@app.route('/delete_payment', methods=['POST'])
def delete_payment():
    payment_id = int(request.form['paymentId'])
    if payment_id < len(payments):
        payments.pop(payment_id)
        flash('Payment deleted successfully!')
    else:
        flash('Payment not found!')
    return redirect(url_for('home'))

@app.route('/view_payment', methods=['POST'])
def view_payment():
    payment_client = request.form['paymentClient']
    client_payments = [p for p in payments if p['client'] == payment_client]
    if client_payments:
        flash(f"Payment History: {client_payments}")
    else:
        flash('No payments found for this client!')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
