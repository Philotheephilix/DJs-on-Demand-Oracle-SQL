
from flask import Flask, render_template, request, redirect, url_for, flash

import dbConnect

app = Flask(__name__)
app.secret_key = 'supersecretkey'  
db_config = dbConnect.read_db_config()
dbConnect.execute_sql(db_config,"SELECT * from studentmaster") 
djs = []
clients = []
events = []
bookings = []
payments = []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_dj', methods=['POST'])
def add_dj():
    dj_name = request.form['djName']
    dj_genre = request.form['djGenre']
    dj_experience = request.form['djExperience']
    djs.append({'name': dj_name, 'genre': dj_genre, 'experience': dj_experience})
    flash('DJ added successfully!')
    print(dj_name,dj_genre,dj_genre,dj_experience)
    dbConnect.executeSQL("query")
    return redirect(url_for('home'))

@app.route('/update_dj', methods=['POST'])
def update_dj():
    dj_id = int(request.form['djId'])
    if dj_id < len(djs):
        djs[dj_id] = {
            'name': request.form['djName'],
            'genre': request.form['djGenre'],
            'experience': request.form['djExperience']
        }
        flash('DJ updated successfully!')
    else:
        flash('DJ not found!')
    return redirect(url_for('home'))

@app.route('/delete_dj', methods=['POST'])
def delete_dj():
    dj_id = int(request.form['djId'])
    if dj_id < len(djs):
        djs.pop(dj_id)
        flash('DJ deleted successfully!')
    else:
        flash('DJ not found!')
    return redirect(url_for('home'))

@app.route('/view_dj', methods=['POST'])
def view_dj():
    dj_id = int(request.form['djId'])
    if dj_id < len(djs):
        flash(f"DJ Profile: {djs[dj_id]}")
    else:
        flash('DJ not found!')
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
    event_name = request.form['eventName']
    event_date = request.form['eventDate']
    event_location = request.form['eventLocation']
    assigned_dj = request.form['assignedDJ']
    events.append({'name': event_name, 'date': event_date, 'location': event_location, 'dj': assigned_dj})
    flash('Event created successfully!')
    return redirect(url_for('home'))

@app.route('/update_event', methods=['POST'])
def update_event():
    event_id = int(request.form['eventId'])
    if event_id < len(events):
        events[event_id] = {
            'name': request.form['eventName'],
            'date': request.form['eventDate'],
            'location': request.form['eventLocation'],
            'dj': request.form['assignedDJ']
        }
        flash('Event updated successfully!')
    else:
        flash('Event not found!')
    return redirect(url_for('home'))

@app.route('/cancel_event', methods=['POST'])
def cancel_event():
    event_id = int(request.form['eventId'])
    if event_id < len(events):
        events.pop(event_id)
        flash('Event cancelled successfully!')
    else:
        flash('Event not found!')
    return redirect(url_for('home'))

@app.route('/view_event', methods=['POST'])
def view_event():
    event_id = int(request.form['eventId'])
    if event_id < len(events):
        flash(f"Event Details: {events[event_id]}")
    else:
        flash('Event not found!')
    return redirect(url_for('home'))

# Booking Management Routes
@app.route('/new_booking', methods=['POST'])
def new_booking():
    booking_client = request.form['bookingClient']
    booking_event = request.form['bookingEvent']
    booking_dj = request.form['bookingDJ']
    booking_date = request.form['bookingDate']
    bookings.append({'client': booking_client, 'event': booking_event, 'dj': booking_dj, 'date': booking_date})
    flash('Booking created successfully!')
    return redirect(url_for('home'))

@app.route('/update_booking', methods=['POST'])
def update_booking():
    booking_id = int(request.form['bookingId'])
    if booking_id < len(bookings):
        bookings[booking_id] = {
            'client': request.form['bookingClient'],
            'event': request.form['bookingEvent'],
            'dj': request.form['bookingDJ'],
            'date': request.form['bookingDate']
        }
        flash('Booking updated successfully!')
    else:
        flash('Booking not found!')
    return redirect(url_for('home'))

@app.route('/cancel_booking', methods=['POST'])
def cancel_booking():
    booking_id = int(request.form['bookingId'])
    if booking_id < len(bookings):
        bookings.pop(booking_id)
        flash('Booking cancelled successfully!')
    else:
        flash('Booking not found!')
    return redirect(url_for('home'))

@app.route('/view_booking', methods=['POST'])
def view_booking():
    booking_id = int(request.form['bookingId'])
    if booking_id < len(bookings):
        flash(f"Booking Details: {bookings[booking_id]}")
    else:
        flash('Booking not found!')
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
