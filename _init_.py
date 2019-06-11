from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


#---------------------------------------Homepage---------------------------------------
#homepage
@app.route("/")
def homepage():
	return render_template('index.html', name=None)
	
#---------------------------------------Staff------------------------------------------	
#show a menu for staff	
@app.route("/staffmenu")
def staffmenu():
	return render_template('staffmenu.html', name=None)

### Movie
#add a movie 
@app.route('/staffaddmovie')
def staffaddmovie(name=None):
    return render_template('staffaddmovieform.html', name=name)

@app.route('/staffaddmovie1', methods=["POST"])
def staffaddmovie1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie (idMovie, MovieName, MovieYear) "
        "VALUES (%s, %s, %s)"
    )
    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#delete a movie	
@app.route('/staffdeletemovie')  
def staffdeletemovie (name=None):  
    return render_template('staffdeletemovieform.html', name=name)   
 
@app.route('/staffdeletemovie1', methods=["POST"])
def staffdeletemovie1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Movie WHERE idMovie = %s"  
    )
    data = (request.form['idMovie'],) 
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#modify a movie
@app.route('/staffmodifymovie')
def staffmodifymovie (name=None):
    return render_template('staffmodifymovieform.html', name=name)

@app.route('/staffmodifymovie1', methods=["POST"])
def staffmodifymovie1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    MovieName1 =request.form['MovieName']
    idMovie1 = request.form['idMovie']
    MovieYear1 = request.form['MovieYear']
    modify_stmt = ( 
		"UPDATE Movie SET MovieName= %s, MovieYear = %s WHERE idMovie = %s "	
    )
    data = (MovieName1,MovieYear1,idMovie1)
    cursor.execute(modify_stmt,data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#list all movies 
@app.route("/stafflistmovie")
def stafflistmovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT MovieName, idMovie, MovieYear from Movie ORDER BY MovieName")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('staffmovielistform.html',users=users)
 

###Genres
#add a genre
@app.route('/staffaddgenre')
def staffaddgenre(name=None):
    return render_template('staffaddgenreform.html', name=name)
	
@app.route('/staffaddgenre1', methods=["POST"])
def staffaddgenre1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Genre (Movie_idMovie, Genre) "
        "VALUES (%s, %s)"
    )
    data = (request.form['Movie_idMovie'], request.form['Genre'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)
	

# delete a genre
@app.route('/staffdeletegenre')  
def staffdeletegenre (name=None):  
    return render_template('staffdeletegenreform.html', name=name) 
	
@app.route('/staffdeletegenre1', methods=["POST"])
def staffdeletegenre1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Genre WHERE Movie_idMovie = %s" 
    )
    data = (request.form['Movie_idMovie'],)
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)
	

#list all genres and movie names
@app.route('/stafflistmoviegenre')
def stafflistmoviegenre ():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    #query = ("SELECT Genre, MovieName from ShowingInfo ORDER BY Genre")
    query = ("SELECT Genre, MovieName FROM Movie, Genre WHERE Movie_idMovie = idMovie ORDER BY Genre")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('staffmoviegenrelistform.html',users=users)
	
###Rooms
#add a room 
@app.route('/staffaddroom')
def staffaddroom(name=None):
    return render_template('staffaddroomform.html', name=name)
	
@app.route('/staffaddroom1', methods=["POST"])
def staffaddroom1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO TheatreRoom (RoomNumber, Capacity) "
        "VALUES (%s, %s)"
    )
    data = (request.form['RoomNumber'], request.form['Capacity'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#delete a room  
@app.route('/staffdeleteroom')  
def staffdeleteroom (name=None):  
    return render_template('staffdeleteroomform.html', name=name)   
    

@app.route('/staffdeleteroom1', methods=["POST"])
def staffdeleteroom1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM TheatreRoom WHERE RoomNumber = %s" 
    )
    data = (request.form['RoomNumberBox'],)
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

	
#modify a room
@app.route('/staffmodifyroom')
def staffmodifyroom (name=None):
    return render_template('staffmodifyroomform.html', name=name)

@app.route('/staffmodifyroom1', methods=["POST"])
def staffmodifyroom1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    RoomNumber1 =request.form['RoomNumber']
    Capacity1 = request.form['Capacity']
    modify_stmt = ( 
		"UPDATE TheatreRoom SET Capacity= %s  WHERE RoomNumber = %s "	
    )
    data = (Capacity1,RoomNumber1)
    cursor.execute(modify_stmt,data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#list all rooms	
@app.route("/stafflistroom")
def stafflistroom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from TheatreRoom")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('staffroomlistform.html',users=users)

	
###Showings
#add a showing
@app.route('/staffaddshowing')
def staffaddshowing(name=None):
    return render_template('staffaddshowingform.html', name=name)
	
@app.route('/staffaddshowing1', methods=["POST"])
def staffaddshowing1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Showing (idShowing, ShowingDateTime, Movie_idMovie, TheatreRoom_RoomNumber, TicketPrice) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    data = (request.form['idShowing'], request.form['ShowingDateTime'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'], request.form['TicketPrice'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#delete a showing   
@app.route('/staffdeleteshowing')  
def staffdeleteshowing (name=None):  
    return render_template('staffdeleteshowingform.html', name=name)   
    

@app.route('/staffdeleteshowing1', methods=["POST"])
def staffdeleteshowing1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Showing WHERE idShowing = %s" 
    )
    data = (request.form['idShowing'],)
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)
    

#modify a showing
@app.route('/staffmodifyshowing')
def staffmodifyshowing (name=None):
    return render_template('staffmodifyshowingform.html', name=name)
	
@app.route('/staffmodifyshowing1', methods=["POST"])
def staffmodifyshowing1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    idShowing1 = request.form['idShowing']
    ShowingDateTime1 = request.form['ShowingDateTime']
    Movie_idMovie1 =request.form['Movie_idMovie']
    TheatreRoom_RoomNumber1 =request.form['TheatreRoom_RoomNumber']
    TicketPrice1 =request.form['TicketPrice']
    modify_stmt = ( 
		"UPDATE Showing SET ShowingDateTime = %s, Movie_idMovie = %s , TheatreRoom_RoomNumber = %s , TicketPrice = %s WHERE idShowing = %s "
    )
    data = (ShowingDateTime1,Movie_idMovie1,TheatreRoom_RoomNumber1,TicketPrice1,idShowing1)
    cursor.execute(modify_stmt,data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#list all showings	
@app.route('/stafflistshowing')
def sstafflistshowing ():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT ShowingDateTime, idShowing, Movie_idMovie, TheatreRoom_RoomNumber, TicketPrice from Showing ORDER BY ShowingDateTime")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('staffshowinglistform.html',users=users)



###Customers
#add a customer
@app.route('/staffaddcustomer')
def staffaddcustomer(name=None):
    return render_template('staffaddcustomerform.html', name=name)
	
@app.route('/staffaddcustomer1', methods=["POST"])
def staffaddcustomer1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Customer (idCustomer, FirstName, LastName, EmailAddress, Sex) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    data = (request.form['idCustomer'], request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)
	
#delete a customer	
@app.route('/staffdeletecustomer')  
def staffdeletecustomer ():  
    return render_template('staffdeletecustomerform.html')   

@app.route('/staffdeletecustomer1', methods=["POST"])
def staffdeletecustomer1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Customer WHERE idCustomer = %s" 
    )
    data = (request.form['idCustomer'],)
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)
	
#modify a customer
@app.route('/staffmodifycustomer')
def staffmodifycustomer (name=None):
    return render_template('staffmodifycustomerform.html', name=name)

@app.route('/staffmodifycustomer1', methods=["POST"])
def staffmodifycustomer1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    idCustomer1 = request.form['idCustomer']
    FirstName1 = request.form['FirstName']
    LastName1 =request.form['LastName']
    EmailAddress1 =request.form['EmailAddress']
    Sex1 =request.form['Sex']
    modify_stmt = ( 
		"UPDATE Customer SET FirstName = %s, LastName = %s,EmailAddress = %s, Sex = %s  WHERE idCustomer = %s "
    )
    data = (FirstName1,LastName1,EmailAddress1,Sex1,idCustomer1)
    cursor.execute(modify_stmt,data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

#list all customers	
@app.route('/stafflistcustomer')
def stafflistcustomer ():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT LastName, FirstName, idCustomer, EmailAddress, Sex from Customer ORDER BY LastName")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('staffcustomerlistform.html',users=users)


###Attend
#list all information order by rating
@app.route('/staffattendlistall')
def staffattendlistall ():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select idCustomer, FirstName, LastName, idShowing, ShowingDateTime, MovieName, rating from Attend, Customer, Showing, Movie where idCustomer = Customer_idCustomer AND Showing_idShowing = idShowing AND Movie_idMovie = idMovie ORDER BY rating")
    cursor.execute(query)
    users=cursor.fetchall()
    cnx.close()
    return render_template('staffattendlistallform.html',users=users)
    
#delete from Attend 
@app.route('/staffdeletefromattend')  
def staffdeletefromattend (name=None):  
    return render_template('staffdeletefromattendform.html', name=name)   

@app.route('/staffdeletefromattend1', methods=["POST"])
def staffdeletefromattend1():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    delete_stmt = (
        "DELETE FROM Attend WHERE Customer_idCustomer = %s and Showing_idShowing = %s " 
    )
    data = (request.form['idCustomer1'],request.form['idshowing1'])
    cursor.execute(delete_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('staffmenu.html', name=None)

 
#---------------------------------------Customer------------------------------------------
#show a menu for customer
@app.route("/usermenu")
def usermenu():
	return render_template('usermenu.html', name=None)

####### User Select Movie #######
@app.route("/userselectgenremovie")
def userSelectMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("select distinct genre from Genre")
    cursor.execute(insert_stmt)
    genretype = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userselectgenremovie.html', genretype = genretype)


@app.route('/submituserselectgenremovie', methods=["POST"])
def submitUserSelectGenreMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    genreform = request.form.get('selectgenre')
    startdateform1 = request.form.get('startDateBox')
    enddateform1 = request.form.get('endDateBox')
    isSeatform = request.form.get('isSeatBox')
    nameform = request.form['movieNameBox']
    if isSeatform:
        query = ("SELECT * from ShowingInfo where Genre = %s and ShowingDateTime >=  %s  and ShowingInfo.ShowingDateTime <= %s and SeatRemained > 0")
        startdateform = startdateform1 + " 00:00:00"
        enddateform = enddateform1 + " 23:59:59" 
        data = (genreform,startdateform,enddateform)
    if not nameform : 
        query = ("SELECT * from ShowingInfo where Genre = %s and ShowingDateTime >=  %s and ShowingInfo.ShowingDateTime <= %s and SeatRemained > 0")
        startdateform = startdateform1 + " 00:00:00"
        enddateform = enddateform1 + " 23:59:59" 
        data = (genreform,startdateform,enddateform)
    else:
        query = ("SELECT * from ShowingInfo where MovieName = %s")
        data = (nameform,)
    cursor.execute(query,data)
    queryresult = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userselectresult.html',queryresult = queryresult)

####### User Select Movie #######
@app.route("/userselectgenremovieinjection")
def userSelectMovieInjection():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("select distinct genre from Genre")
    cursor.execute(insert_stmt)
    genretype = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userselectgenremovieinjection.html', genretype = genretype)


@app.route('/submituserselectgenremovieinjection', methods=["POST"])
def submitUserSelectGenreMovieInjection():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    genreform = request.form.get('selectgenre')
    startdateform = request.form.get('startDateBox')
    enddateform = request.form.get('endDateBox')
    isSeatform = request.form.get('isSeatBox')
    nameform = request.form['movieNameBox']
    query = ("SELECT * from ShowingInfo where MovieName = '" + nameform +"'")
    cursor.execute(query)
    queryresult = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userselectresultinjection.html',queryresult = queryresult)


####### User Attend a Showing(buy ticket)  #######
@app.route("/userbuyticket")
def userBuyTicket():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    namequery1 = ("select FirstName,LastName from Customer")
    cursor.execute(namequery1)
    customername1 = cursor.fetchall()
    showingquery1 = ("select idShowing from Showing")
    cursor.execute(showingquery1)
    showingid1 = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userbuyticket.html', customername1 = customername1, showingid1 = showingid1)


@app.route('/submituserselectname', methods=["POST"])
def submitUserSelectName():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    name = request.form.get('selectfirstname')
    name1 = name.split(' ')
    first1 = name1[1]
    last1 = name1[2]
    showingid1 = request.form.get('selectshowingid')
    query = ("SELECT idCustomer from Customer where FirstName = %s and LastName = %s ")
    data = (first1,last1)
    cursor.execute(query,data)
    idresult1 = cursor.fetchone()
    idresult = str(idresult1[0])
    insert_stmt = (
        "INSERT INTO Attend (Customer_idCustomer, Showing_idShowing) "
        "VALUES (%s, %s)"
    )
    data = (idresult,showingid1)
    cursor.execute(insert_stmt, data)
    query1 = ("SELECT * from Attend where Customer_idCustomer = %s ")
    data1 = (idresult,)
    cursor.execute(query1,data1)
    ticketresult = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userbuyticketresult.html',ticketresult = ticketresult)





####### User Rate a movie #######
@app.route("/userratemovie")
def userRateMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    namequery1 = ("select FirstName,LastName from Customer")
    cursor.execute(namequery1)
    customername1 = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userratemovie.html', customername1 = customername1)


@app.route('/submituserratemovie1', methods=["POST"])
def submitUserRateResult():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    name = request.form.get('selectfirstname')
    name1 = name.split(' ')
    first1 = name1[1]
    last1 = name1[2]
    showingid1 = request.form.get('selectshowingid')
    query = ("SELECT idCustomer from Customer where FirstName = %s and LastName = %s")
    data1 = (first1,last1)
    cursor.execute(query,data1)
    idresult1 = cursor.fetchone()
    idresult = str(idresult1[0])
    #get showing information
    query1 = ("SELECT Showing_idShowing,MovieName from AttendShowingInfo where Customer_idCustomer = %s")
    data2 = (idresult,)
    cursor.execute(query1,data2)
    showingmoviename1 = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('usersrateresult.html',showingmoviename1 = showingmoviename1,idresult = idresult)


@app.route('/submituserratemovie2', methods=["POST"])
def submitUserRateResult2():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    form1a = request.form.get('showinginfo1')
    form1b = form1a.split(' ', 2);
    showingid = form1b[1]
    ratenum = request.form.get('ratebox')
    customid = request.form.get('customidbox')

    update_stmt = (
        "UPDATE Attend SET Rating= %s WHERE Customer_idCustomer = %s and Showing_idShowing = %s "
    )
    data1 = (ratenum,customid,showingid)
    cursor.execute(update_stmt,data1)

    query1 = ("SELECT * from Attend where Customer_idCustomer = %s ")
    data2 = (customid,)
    cursor.execute(query1,data2)
    rateupdate = cursor.fetchall()
    cnx.commit()
    cnx.close()

    return render_template('usersrateresult1.html',rateupdate = rateupdate)


####### User review Showing #######
@app.route("/userreviewshowing")
def userReviewShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    namequery1 = ("select FirstName,LastName from Customer")
    cursor.execute(namequery1)
    customername1 = cursor.fetchall()
    showingquery1 = ("select idShowing from Showing")
    cursor.execute(showingquery1)
    showingid1 = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userreviewshowing.html', customername1 = customername1, showingid1 = showingid1)

@app.route('/submituserreviewshowing', methods=["POST"])
def submitUserReviewShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    name = request.form.get('selectfirstname')
    name1 = name.split(' ')
    first1 = name1[1]
    last1 = name1[2]
    showingid1 = request.form.get('selectshowingid')
    query = ("SELECT idCustomer from Customer where FirstName =  %s  and LastName =  %s  ")
    data1 = (first1,last1)
    cursor.execute(query,data1)
    idresult1 = cursor.fetchone()
    idresult = str(idresult1[0])

    namequery1 = ("SELECT Customer_idCustomer,Showing_idShowing, Rating, MovieName from AttendShowingInfo where Customer_idCustomer = %s ")
    data2 = (idresult,)
    cursor.execute(namequery1,data2)
    customerinfo = cursor.fetchall()

    cnx.commit()
    cnx.close()
    return render_template('userreviewshowingresult.html',customerinfo = customerinfo)

####### User review Showing #######
@app.route("/userpersonalinfo")
def userPersonalInfo():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    namequery1 = ("select FirstName,LastName from Customer")
    cursor.execute(namequery1)
    customername1 = cursor.fetchall()
    showingquery1 = ("select idShowing from Showing")
    cursor.execute(showingquery1)
    showingid1 = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userpersonalinfo.html', customername1 = customername1, showingid1 = showingid1)

@app.route('/submituserpersonalinfo', methods=["POST"])
def submitUserPersonInfo():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    name = request.form.get('selectfirstname')
    name1 = name.split(' ')
    first1 = name1[1]
    last1 = name1[2]
    showingid1 = request.form.get('selectshowingid')
    query = ("SELECT idCustomer from Customer where FirstName = %s and LastName = %s ")
    data1 = (first1,last1)
    cursor.execute(query,data1)
    idresult1 = cursor.fetchone()
    idresult = str(idresult1[0])
    namequery1 = ("SELECT * from Customer where idCustomer = %s ")
    data2 = (idresult,)
    cursor.execute(namequery1,data2)
    personinfo = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('userpersoninforesult.html',personinfo = personinfo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
