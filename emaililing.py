from email.message import EmailMessage
import imghdr
import smtplib

PASSWORD = "" ""# You need to turn on two-step verification.
SENDER = "" # Put here the email that you would like to send it.
RECEIVER = "" # Put here the email that you would like to receive it.

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer")
    print("send_email function ended")
    
    
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


#test
if __name__ == "__main__":
    send_email(image_path="")
