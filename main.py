import smtplib
import datetime as dt
import random

now = dt.datetime.now()
curr_day = now.isoweekday()     #Returns an integer value determining (mon-sun)->(1-7)
if curr_day % 7 == 1:  #Condition to check if it's monday or not
    with open("quotes.txt") as file:
        read = file.readlines()
        quote = read[random.randint(0, len(read)-1)]
        my_email = "mymail@gmail.com"  #Your Mail
        password = "pslq lqke wuay wirp"        #Add the 16-char password you get after creating an external app password for ur mail
        with smtplib.SMTP("smtp.gmail.com", port = 587)  as connection:       #Port 25 is used usually, port 587 used to segregate from the traffic
            connection.starttls()       #For securing the connection through encryption
            connection.login(user = my_email, password = password)
            connection.sendmail(from_addr = my_email,
                                to_addrs = "mail1@gmail.com",       #Receiver's mail
                                msg = f"Subject:Monday motivational quote's here\n\n{quote}")

