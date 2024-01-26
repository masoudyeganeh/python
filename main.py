# imports for SQL data part
import pyodbc
from datetime import datetime, timedelta
import pandas as pd

# imports for sending email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-5QDCU54;"
            "Database=Northwind;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

# cursor.execute("SELECT TOP(100) * FROM dbo.Orders")

# data = pd.read_sql("SELECT TOP(100) * FROM dbo.Orders", cnxn)

# print(data)

# date = datetime.today() - timedelta(days=7)  # get the date 7 days ago
#
# date = date.strftime("%Y-%m-%d")  # convert to format yyyy-mm-dd

cnxn = pyodbc.connect(cnxn_str)  # initialise connection (assume we have already defined cnxn_str)

country = "France"

# build up our query string
query = ("SELECT count(*) FROM dbo.Orders "
         f"WHERE shipCountry = '{country}'")

# execute the query and read to a dataframe in Python
data = pd.read_sql(query, cnxn)

del cnxn  # close the connection

# make a few calculations
# mean_payment = data['payment'].mean()
# std_payment = data['payment'].std()
#
# # get max payment and product details
# max_vals = data[['product', 'payment']].sort_values(by=['payment'], ascending=False).iloc[0]

# write an email message
txt = (f"Hi the number of orders from France is {data}"
       )

# we will built the message using the email library and send using smtplib
msg = MIMEMultipart()
msg['Subject'] = "Automated customer report"  # set email subject
msg.attach(MIMEText(txt))  # add text contents

# we will send via outlook, first we initialise connection to mail server
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()  # say hello to the server
smtp.starttls()  # we will communicate using TLS encryption

# login to outlook server, using generic email and password
smtp.login('masoudyeganeh92@gmail.com', 'Et@8101819')

# send email to our boss
smtp.sendmail('masoudyeganeh92@gmail.com', 'masoudev@gmail.com', msg.as_string())

# finally, disconnect from the mail server
smtp.quit()
