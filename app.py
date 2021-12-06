from flask import Flask,render_template, redirect, request,url_for,flash
import smtplib
from email.message import EmailMessage
from flask_sqlalchemy import  SQLAlchemy
from datetime import datetime
import psycopg2


app = Flask(__name__)

# seeting the secret key
app.secret_key = 'random string'
ENV = "dev"

if ENV  == "dev":
    app.debug= True
    # delvelopment  database setup
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1236@localhost/postgres'


else:
    app.debug=False
    # deploying database here
    app.config['SQLALCHEMY_DATABASE_URI']="postgresql://dsmhjyafxvmcbm:3d14452c1a7bcca4f10f2d867dce0d1048b8d3b5e13f4fc02f8bb84da9426243@ec2-54-235-45-88.compute-1.amazonaws.com:5432/d39sji5mla3efs"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initilizing the database
db = SQLAlchemy(app)

class Feedback(db.Model):

    __tablename__= 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=200), nullable=False)
    food = db.Column(db.String(length=200), nullable=False)
    location = db.Column(db.String(length=200), nullable=False)
    hostelOrOffice = db.Column(db.String(length=200), nullable=False)
    package = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.Integer, nullable=False )
    email = db.Column(db.String(length=100), nullable=False)
    restaurant = db.Column(db.String(length=100), nullable=False)



    def __init__(self,name,food,location,hostelOrOffice,package,contact,email,restaurant):
        self.name = name
        self.food = food
        self.location = location
        self.hostelOrOffice = hostelOrOffice
        self.package = package
        self.contact = contact
        self.email = email
        self.restaurant = restaurant


    def __repr__(self):
        return 'Records_id: ' + str(self.id)






# sayinh hrllo snf putting the name of the user on the website
@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")




@app.route('/menu',  methods = ["POST", "GET"])
def menu():
    return render_template("menu2.html")

@app.route('/delivery',  methods = ["POST", "GET"])
def delivery():
    flash("Please place your order first? " ,category="danger")
    return redirect(url_for('menu'))


@app.route('/deliveryForRoyal', methods = ['POST', 'GET'])
def deliveryForRoyal():
    #if request.method == "POST":
       return render_template("deliveryForRoyal.html")
    #else:
    #   flash("Please place your order first? ", category="danger")
    #   return redirect(url_for("deliveryForRoyal.html"))



@app.route('/deliveryForRoyalForm', methods = ['POST', 'GET'])
def deliveryForRoyalForm():
    if request.method == 'POST':
        name = request.form.get("name")
        food = request.form.get("food")
        location= request.form.get("location")
        hostelorOffice = request.form.get("hostelorOfficeNum")
        pack = request.form.get("number")
        phonenumber=request.form.get("phoneNumber")
        email = request.form.get("email")
        restaurant = "Royal Food Court"

        # VALIDATING THE USER INPUT TO SEE IF ALL THE PARIMETER IS BEEN GIVEN
        if name == "" or phonenumber == "" or email == "" or pack == "" or hostelorOffice == "" or location == "" or food == "":
            flash(f"please fill in all the credentials. try again!! ", category="danger")
            return redirect(url_for('deliveryForRoyal'))
        try:
            # saving to the database
            data = Feedback(name,food,location,hostelorOffice,pack,phonenumber,email,restaurant)
            # to add the data
            db.session.add(data)
            db.session.commit()
            databaseMessage="succssful"
        except:
            databaseMessage ="failed"
            

        print(name, food, location, hostelorOffice, pack,phonenumber,email)

        admins = ["alexanderemmanuel1719@gmail.com", "samuel.oep3@gmail.com","Usmanfawaz68@gmail.com","sheddydavid@gmail.com"]
        customerMessage = f"My name : {name} \n my phone number: {phonenumber} \nmy email: {email} \n location: {location} \n hostel/Office: {hostelorOffice} \nhostel/Office NUm: {pack} \n Food: {food} \n Restaurant: {restaurant}\n database: {databaseMessage}"
        
        try:
            for admin in admins:

                # initialize the server and the gate wway
                server = smtplib.SMTP('smtp.gmail.com', 587)

                # telling the server it is secure
                server.starttls()

                # login in , which will need your email and your password
                server.login("websitewebsite944@gmail.com", "1236Jesus")
                # setting the email subject or title
                emailSender = EmailMessage()
                # the person sending the message
                emailSender['From'] = "websitewebsite944@gmail.com"
                # to whom you want to send the message to
                emailSender["To"] = admin
                emailSender["Subject"] = "MethodistRestaurant Delivery Service"

                emailSender.set_content(customerMessage)
                server.send_message(emailSender)

            """ server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()"""

            # server.sendmail("websitewebsite944@gmail.com", admin, customerMessage)
            flash(f"Your {food} order was sucessful! Your package would be delivered in less than 10 minutes. Thanks ",
                  category="success")
            return redirect(url_for('home'))
        except:
            flash(f"please something went wrong try again!! (Hint: Check Your Internet Connection)", category="danger")
            return redirect(url_for('deliveryForRoyal'))



        #return redirect(url_for('home'))
    else:
        flash("Please place your order first? ", category="danger")
        return redirect(url_for('menu'))





# delivery for kiberb(suya)
@app.route('/deliveryForKiberb', methods = ['POST', 'GET'])
def deliveryForKiberb():
    #if request.method == "POST":
       return render_template("deliveryForKiberb.html")
    #else:
    #   flash("Please place your order first? ", category="danger")
    #   return redirect(url_for('menu'))



@app.route('/deliveryForKiberbForm', methods = ['POST', 'GET'])
def deliveryForKiberbForm():
    if request.method == 'POST':
        name = request.form.get("name")
        food = request.form.get("food")
        location= request.form.get("location")
        hostelorOffice = request.form.get("hostelorOfficeNum")
        pack = request.form.get("number")
        phonenumber=request.form.get("phoneNumber")
        email = request.form.get("email")
        restaurant = "Kilbarb shop"

        # VALIDATING THE USER INPUT TO SEE IF ALL THE PARIMETER IS BEEN GIVEN
        if name=="" or  phonenumber =="" or email =="" or pack=="" or hostelorOffice=="" or location=="" or food=="":
            flash(f"please fill in all the credentials. try again!! ", category="danger")
            return redirect(url_for('deliveryForKiberb'))
        try:
            # saving to the database
            data = Feedback(name,food,location,hostelorOffice,pack,phonenumber,email,restaurant)
            # to add the data
            db.session.add(data)
            db.session.commit()
            databaseMessage="succssful"
        except:
            databaseMessage="failed"



        print(name, food, location, hostelorOffice, pack,phonenumber,email)

        admins = ["alexanderemmanuel1719@gmail.com", "samuel.oep3@gmail.com","Usmanfawaz68@gmail.com","sheddydavid@gmail.com"]
        customerMessage = f"My name : {name} \n my phone number: {phonenumber} \nmy email: {email} \n location: {location} \n hostel/Office: {hostelorOffice} \nPack: {pack} \n Food: {food} \nRestaurant: {restaurant}\n database:{databaseMessage}"
        try:
            
            for admin in admins:
                # initialize the server and the gate wway
                server = smtplib.SMTP('smtp.gmail.com', 587)

                # telling the server it is secure
                server.starttls()

                # login in , which will need your email and your password
                server.login("websitewebsite944@gmail.com", "1236Jesus")
                # trying to send mail to the person in charge of taking it to book
                # setting the email subject or title
                emailSender = EmailMessage()
                # the person sending the message
                emailSender['From'] = "websitewebsite944@gmail.com"
                # to whom you want to send the message to
                emailSender["To"] = admin
                emailSender["Subject"] = "MethodistRestaurant Delivery Service"

                emailSender.set_content(customerMessage)
                server.send_message(emailSender)

            """ server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()"""

            # server.sendmail("websitewebsite944@gmail.com", admin, customerMessage)
            flash(f"Your {food} order was sucessful! Your package would be delivered in less than 10 minutes. Thanks ",
                  category="success")
            return redirect(url_for('home'))
        except:
            flash(f"please something went wrong try again!! (Hint: Check Your Internet Connection)", category="danger")
            return redirect(url_for('deliveryForKiberb'))


        #return redirect(url_for('home'))
    else:
        flash("Please place your order first? ", category="danger")
        return redirect(url_for('menu'))



@app.route('/deliveryForManovia', methods = ['POST', 'GET'])
def deliveryForManovia():
    #if request.method == 'POST':
        return render_template("deliveryForManovia.html")
    #else:
    #   flash("Please place your order first? ", category="danger")
    #   return redirect(url_for('menu'))


@app.route('/deliveryForManoviaForm', methods = ['POST', 'GET'])
def deliveryForManoviaForm():
    if request.method == 'POST':
        name = request.form.get("name")
        food = request.form.get("food")
        location= request.form.get("location")
        hostelorOffice = request.form.get("hostelorOfficeNum")
        pack = request.form.get("number")
        phonenumber=request.form.get("phoneNumber")
        email = request.form.get("email")
        restaurant = "Manovia restaurant"

        # VALIDATING THE USER INPUT TO SEE IF ALL THE PARIMETER IS BEEN GIVEN
        if name=="" or  phonenumber =="" or email =="" or pack=="" or hostelorOffice=="" or location=="" or food=="":
            flash(f"please fill in all the credentials. try again!! ", category="danger")
            return redirect(url_for('deliveryForManovia'))

        try:
            # saving to the database
            data = Feedback(name, food, location, hostelorOffice, pack, phonenumber, email, restaurant)
            # to add the data
            db.session.add(data)
            db.session.commit()
            databaseMessage="successful"
        except:
            databaseMessage="failed"

        print(name, food, location, hostelorOffice, pack,phonenumber,email)

        admins = ["alexanderemmanuel1719@gmail.com", "samuel.oep3@gmail.com","Usmanfawaz68@gmail.com","sheddydavid@gmail.com"]
        customerMessage = f"My name : {name} \n my phone number: {phonenumber} \nmy email: {email} \n location: {location} \n hostel/Office: {hostelorOffice} \nPack: {pack} \n Food: {food} \nRestaurant: {restaurant}\n database: {databaseMessage}"

        try:
            
            for admin in admins:
                # initialize the server and the gate wway
                server = smtplib.SMTP('smtp.gmail.com', 587)

                # telling the server it is secure
                server.starttls()

                # login in , which will need your email and your password
                server.login("websitewebsite944@gmail.com", "1236Jesus")
                # trying to send mail to the person in charge of taking it to book
                # setting the email subject or title
                emailSender = EmailMessage()
                # the person sending the message
                emailSender['From'] = "websitewebsite944@gmail.com"
                # to whom you want to send the message to
                emailSender["To"] = admin
                emailSender["Subject"] = "MethodistRestaurant Delivery Service"

                emailSender.set_content(customerMessage)
                server.send_message(emailSender)

            """ server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()"""

            # server.sendmail("websitewebsite944@gmail.com", admin, customerMessage)
            flash(f"Your {food} order was sucessful! Your package would be delivered in less than 10 minutes. Thanks ",
                  category="success")
            return redirect(url_for('home'))
        except:
            flash(f"please something went wrong try again!! (Hint: Check Your Internet Connection)", category="danger")
            return redirect(url_for('deliveryForManovia'))

        # return redirect(url_for('home'))

        #return redirect(url_for('home'))
    else:
        flash("Please place your order first? ", category="danger")
        return redirect(url_for('menu'))






@app.route('/deliveryForMartharus', methods = ['POST', 'GET'])
def deliveryForMartharus():
    #if request.method=='POST':
       return render_template("deliveryForMartharus.html")
    #else:
     #  flash("Please place your order first? ", category="danger")
     #  return redirect(url_for('menu'))


@app.route('/deliveryForMartharusForm', methods = ['POST', 'GET'])
def deliveryForMartharusForm():
    if request.method == 'POST':
        name = request.form.get("name")
        food = request.form.get("food")
        location= request.form.get("location")
        hostelorOffice = request.form.get("hostelorOfficeNum")
        pack = request.form.get("number")
        phonenumber=request.form.get("phoneNumber")
        email = request.form.get("email")
        restaurant = "Matharus"

        # VALIDATING THE USER INPUT TO SEE IF ALL THE PARIMETER IS BEEN GIVEN
        if name=="" or  phonenumber =="" or email =="" or pack=="" or hostelorOffice=="" or location=="" or food=="":
            flash(f"please fill in all the credentials. try again!! ", category="danger")
            return redirect(url_for('deliveryForMartharus'))

        try:
            # saving to the database
            data = Feedback(name, food, location, hostelorOffice, pack, phonenumber, email, restaurant)
            # to add the data
            db.session.add(data)
            db.session.commit()
            databaseMessage="Successful"
        except:
            databaseMessage="Failed"


        print(name, food, location, hostelorOffice, pack,phonenumber,email)

        admins = ["alexanderemmanuel1719@gmail.com", "samuel.oep3@gmail.com","Usmanfawaz68@gmail.com","sheddydavid@gmail.com"]
        customerMessage = f"My name : {name} \n my phone number: {phonenumber} \nmy email: {email} \n location: {location} \n hostel/Office: {hostelorOffice} \nPack: {pack} \n Food: {food} \nRestaurant: {restaurant}\n database: {databaseMessage}"

        try:
            for admin in admins:
                # initialize the server and the gate wway
                server = smtplib.SMTP('smtp.gmail.com', 587)

                # telling the server it is secure
                server.starttls()

                # login in , which will need your email and your password
                server.login("websitewebsite944@gmail.com", "1236Jesus")
                # trying to send mail to the person in charge of taking it to book
                # setting the email subject or title
                emailSender = EmailMessage()
                # the person sending the message
                emailSender['From'] = "websitewebsite944@gmail.com"
                # to whom you want to send the message to
                emailSender["To"] = admin
                emailSender["Subject"] = "MethodistRestaurant Delivery Service"

                emailSender.set_content(customerMessage)
                server.send_message(emailSender)


            """ server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()"""

            #server.sendmail("websitewebsite944@gmail.com", admin, customerMessage)
            flash(f"Your {food} order was sucessful! Your package would be delivered in less than 10 minutes. Thanks ",
                  category="success")
            return redirect(url_for('home'))
        except:
            flash(f"please something went wrong try again!! (Hint: Check Your Internet Connection)", category="danger")
            return redirect(url_for('deliveryForMartharus'))


        #return redirect(url_for('home'))
    else:
        flash("Please place your order first? ", category="danger")
        return redirect(url_for('menu'))






@app.route('/deliveryForStella', methods = ['POST', 'GET'])
def deliveryForStella():
    #if request.method == 'POST':
         return render_template("deliveryForStella.html")
    #elif  request.method == 'GET':
    #    flash("Please place your order first? ", category="danger")
    #    return redirect(url_for('menu'))


@app.route('/deliveryForStellaForm', methods = ['POST', 'GET'])
def deliveryForStellaForm():
    if request.method == 'POST':
        name = request.form.get("name")
        food = request.form.get("food")
        location= request.form.get("location")
        hostelorOffice = request.form.get("hostelorOfficeNum")
        pack = request.form.get("number")
        phonenumber=request.form.get("phoneNumber")
        email = request.form.get("email")
        restaurant = "Stella Dining"


        # VALIDATING THE USER INPUT TO SEE IF ALL THE PARIMETER IS BEEN GIVEN
        if name=="" or  phonenumber =="" or email =="" or pack=="" or hostelorOffice=="" or location=="" or food=="":
            flash(f"please fill in all the credentials. try again!! ", category="danger")
            return redirect(url_for('deliveryForStella'))

        try:
            # saving to the database
            data = Feedback(name, food, location, hostelorOffice, pack, phonenumber, email, restaurant)
            # to add the data
            db.session.add(data)
            db.session.commit()
            databaseMessage="successful"
        except:
            databaseMessage="Failed"




        print(name, food, location, hostelorOffice, pack,phonenumber,email)

        admins = ["alexanderemmanuel1719@gmail.com", "samuel.oep3@gmail.com","Usmanfawaz68@gmail.com","sheddydavid@gmail.com"]
        customerMessage = f"My name : {name} \n my phone number: {phonenumber} \nmy email: {email} \n location: {location}\nhostel/Office: {hostelorOffice}\nPack: {pack}\nFood:{food} \nRestaurant:{restaurant}\n database: {databaseMessage}"

        try:
            for admin in admins:

                # initialize the server and the gate wway
                server = smtplib.SMTP('smtp.gmail.com', 587)

                # telling the server it is secure
                server.starttls()

                # login in , which will need your email and your password
                server.login("websitewebsite944@gmail.com", "1236Jesus")
                # trying to send mail to the person in charge of taking it to book
                # setting the email subject or title
                emailSender = EmailMessage()
                # the person sending the message
                emailSender['From'] = "websitewebsite944@gmail.com"
                # to whom you want to send the message to
                emailSender["To"] = admin
                emailSender["Subject"] = "MethodistRestaurant Delivery Service"

                emailSender.set_content(customerMessage)
                server.send_message(emailSender)

            """ server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()"""

            # server.sendmail("websitewebsite944@gmail.com", admin, customerMessage)
            flash(f"Your {food} order was sucessful! Your package would be delivered in less than 10 minutes. Thanks ",
                  category="success")
            return redirect(url_for('home'))
        except:
            flash(f"please something went wrong try again!! (Hint: Check Your Internet Connection)", category="danger")
            return redirect(url_for('deliveryForStella'))


    #return redirect(url_for('home'))
    elif  request.method == 'GET':
        flash("Please place your order first? ", category="danger")
        return redirect(url_for('menu'))









@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")


@app.route('/contactForm', methods = ['POST', 'GET'])
def contactForm():
    if request.method == 'POST':
        name = request.form.get("name")
        phoneNumber=request.form.get("phoneNumber")
        email = request.form.get("email")
        message = request.form.get("message")

        # VALIDATING THE USER INPUT TO SEE IF ALL THE PARIMETER IS BEEN GIVEN
        if name=="" or  phoneNumber =="" or email =="" or message=="":
            flash(f"please fill in all the credentials. try again!! ", category="danger")
            return redirect(url_for('contact'))

        #flash(f"Thanks {name}, Your enquiry is been processed we would get back to you as soon as possible. Thanks Once again ", category="success")
        print(name,phoneNumber,email, message)
        admin = "alexanderemmanuel1719@gmail.com"
        customerMessage = f"My name is {name} \n my phone number: {phoneNumber} \n my email: {email} \n Message: {message} "
        try:

            # initialize the server and the gate wway
            server = smtplib.SMTP('smtp.gmail.com', 587)

            # telling the server it is secure
            server.starttls()

            # login in , which will need your email and your password
            server.login("websitewebsite944@gmail.com", "1236Jesus")
            # trying to send mail to the person in charge of taking it to book
            # setting the email subject or title
            emailSender = EmailMessage()
            # the person sending the message
            emailSender['From'] = "websitewebsite944@gmail.com"
            # to whom you want to send the message to
            emailSender["To"] = admin
            emailSender["Subject"] = "MethodistRestaurant Enquiry"

            emailSender.set_content(customerMessage)
            server.send_message(emailSender)


            """ server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()"""

            #server.sendmail("websitewebsite944@gmail.com", admin, customerMessage)
            flash(
                f"Thanks {name}, Your enquiry is been processed we would get back to you as soon as possible. Thanks Once again ",
                category="success")
            return redirect(url_for('home'))
        except:
            flash(f"please something went wrong try again!! (Hint: Check Your Internet Connection)", category="danger")
            return redirect(url_for('contact'))







if __name__ == '__main__':
    app.run()



