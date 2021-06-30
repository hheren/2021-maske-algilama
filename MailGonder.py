import smtplib

def MailGonder(mesaj):
    content = mesaj
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("hhheeerrr15678@gmail.com","450509600")
    mail.sendmail("hhheeerrr15678@gmail.com","hhheeerrr15678@gmail.com",content)