
from flask import Flask, render_template, request, redirect, url_for, flash
import dbConnect

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_Packages', methods=['POST'])
def add_Packages():
    Packages_name = str(request.form['PackagesName'])
    Low_Range = str(request.form['Low_Range'])
    High_Range = str(request.form['High_Range'])
    query="insert into D_PACKAGES(code,low_range,high_range) values("+Packages_name+","+Low_Range+","+High_Range+")"
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/update_Packages', methods=['POST'])
def update_Packages():
    Packages_name = str(request.form['PackagesName'])
    Low_Range = str(request.form['Low_Range'])
    High_Range = str(request.form['High_Range'])
    query="update D_PACKAGES set low_range ="+Low_Range+", high_range = "+High_Range+" where code = "+Packages_name
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    print(query)
    return render_template('sucess.html')
@app.route('/delete_Packages', methods=['POST'])
def delete_Packages():
    Packages_name = str(request.form['PackagesName'])
    query="DELETE FROM D_PACKAGES WHERE CODE = "+Packages_name
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    print(query)
    return render_template('sucess.html')

@app.route('/view_Packages', methods=['POST'])
def view_Packages():
    Packages_name = request.form['PackagesName']
    query="select * from D_PACKAGES where code="+Packages_name
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    try:
        id, low, high = result[0]
        data = {
        "code": f"{id}",
        "low": f"{low}",
        "high": str(high)
    }   
        return render_template('viewpack.html', data=data)
        
    except:    
        return render_template('404.html')
    

# Client Management Routes
@app.route('/add_client', methods=['POST'])
def add_client():
    client_id=str(request.form["clientId"])
    client_name = request.form['clientName']
    client_email = request.form['clientEmail']
    client_phone =str( request.form['clientPhone'])
    flash('Client added successfully!')
    query="INSERT INTO d_clients(client_number,first_name,last_name,phone,email) VALUES( "+client_id+",'"+client_name+"','"+client_name+"',"+client_phone+",'"+client_email+"')"
    print(query)
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    
    return render_template('sucess.html')
@app.route('/update_client', methods=['POST'])
def update_client():
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
    return render_template('sucess.html')
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
    return render_template('sucess.html')
@app.route('/view_client', methods=['POST'])
def view_client():
    client_id = str(request.form['clientId'])
    query="select * from d_clients where client_number="+client_id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    print(result)
    try:
        id, first_name, last_name, phone, email = result[0]
        data = {
        "name": f"{first_name} {last_name}",
        "phone": phone,
        "id": str(id),
        "email": email
    }
        return render_template('view.html', data=data)
    except:
        return render_template('404.html')
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
    query="INSERT INTO d_events(client_number,id,name,event_date,description,cost,venue_id,package_code,theme_code) VALUES("+CLIENT_NUMBER+","+event_id+",'"+event_name+"',TO_DATE('04-28-2004','mm-dd-yyyy'),'"+event_desc+"',"+event_cost+","+venue+","+PACKAGE_CODE+","+THEME_CODE+")"
    print(query)
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    flash('Event created successfully!')
    return render_template('sucess.html')
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
    query="UPDATE d_events set CLIENT_NUMBER = "+CLIENT_NUMBER+",NAME = '"+event_name+"',EVENT_DATE = TO_DATE('04-28-2004','mm-dd-yyyy'),DESCRIPTION = '"+event_desc+"',COST = "+event_cost+",VENUE_ID = "+venue+",PACKAGE_CODE = "+PACKAGE_CODE+", THEME_CODE = "+THEME_CODE+"WHERE ID = "+event_id
    print(query)
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/cancel_event', methods=['POST'])
def cancel_event():
    event_id = str(request.form['eventId'])
    query="DELETE FROM d_events WHERE ID = "+event_id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/view_event', methods=['POST'])
def view_event():
    event_id = str(request.form['eventId'])
    query="select * from d_events where code="+event_id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    try:
        id, name, date,desc,cost,venue,pack,theme,client = result[0]
        data = {
        "id": f"{id}",
        "name": f"{name}",
        "date": str(date),
        "desc": f"{desc}",
        "cost": f"{cost}",
        "venue": f"{venue}",
        "pack": f"{pack}",
        "theme": f"{theme}",
        "client": f"{client}"
    }   
        return render_template('viewEvent.html', data=data)
        
    except:    
        return render_template('404.html')
    return redirect(url_for('home'))

# Booking Management Routes
@app.route('/new_booking', methods=['POST'])
def new_booking():
    Theme_desc = str(request.form['bookingClient'])
    Theme_id = str(request.form['bookingId'])
    query="INSERT INTO d_themes(code,description) VALUES("+Theme_id+",'"+Theme_desc+"')"
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/update_booking', methods=['POST'])
def update_booking():
    Theme_desc = str(request.form['bookingClient'])
    Theme_id = str(request.form['bookingId'])
    query="UPDATE D_THEMES SET DESCRIPTION = '"+Theme_desc+"' WHERE CODE = "+Theme_id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/cancel_booking', methods=['POST'])
def cancel_booking():
    Theme_id = str(request.form['bookingId'])
    query="DELETE FROM D_THEMES WHERE CODE = "+Theme_id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/view_booking', methods=['POST'])
def view_booking():
    theme_id = str(request.form['bookingId'])
    query="select * from D_THEMES where code="+theme_id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)

    try:
        code, desc = result[0]
        data = {
        "code": f"{id}",
        "desc": f"{desc}"
    }   
        return render_template('viewTheme.html', data=data)
        
    except:    
        return render_template('404.html')
    return redirect(url_for('home'))

# Payment Management Routes
@app.route('/add_CD', methods=['POST'])
def add_CD():
    id = request.form['CDId']
    title = request.form['CDClient']
    year = request.form['CDAmount']
    query="INSERT INTO d_cds(cd_number,title,producer,year) VALUES("+id+",'"+title+"','Old Town Records',"+year+")"
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    flash('Payment added successfully!')
    return render_template('sucess.html')
@app.route('/update_CD', methods=['POST'])
def update_CD():
    id = request.form['CDId']
    title = request.form['CDClient']
    year = request.form['CDAmount']
    query="UPDATE D_CDS SET TITLE = '"+title+"',year = "+year+" WHERE CD_NUMBER = "+id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/delete_CD', methods=['POST'])
def delete_CD():
    id = request.form['CDId']
    query="DELETE FROM D_CDS WHERE CD_NUMBER = "+id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)
    return render_template('sucess.html')
@app.route('/view_CD', methods=['POST'])
def view_CD():
    id = request.form['CDId']
    query="select * from D_CDS where code="+id
    db_config = dbConnect.read_db_config()
    result=dbConnect.execute_sql(db_config,query)

    try:
        id, title, producer,year = result[0]
        data = {
        "id": f"{id}",
        "year": f"{year}",
        "title":f"{title}"
    }   
        return render_template('viewCd.html', data=data)
        
    except:    
        return render_template('404.html')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
