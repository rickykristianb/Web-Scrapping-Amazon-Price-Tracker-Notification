import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
IMAGE = os.getenv('IMAGE')


class Notification:

    def __init__(self, product_name, product_price, product_url):
        self.product_name = product_name
        self.product_price = product_price
        self.product_url = product_url

    def send_notification(self):
        new_message = MIMEMultipart()
        new_message["Subject"] = "Price Down Alert!!"
        new_message["From"] = EMAIL
        new_message["To"] = "ricky.kristianb@gmail.com"

        # email_body = f"""
        # Hi,
        # Take a look for you item
        # {self.product_name}
        # Now price is ${self.product_price}\n
        # Click this link below to check on Amazon Website
        # """
        # NOTE EMAIL BODY IS NOT USED, CHANGE TO HTML NOT PLAIN TEXT

        email_link = f"""
        <html>
            <head>
            </head>
            <body>
                <div>
                    <p>Hi!!</p>
                    <p>Take a look for this Item.</p>
                    <p>"<strong>{self.product_name}</strong>"</p>
                    <img src="cid:image1" alt="Image Not Found" width=500, height=500>
                    <p>Now price is <strong>${self.product_price}</strong></p>
                    <p>Click this link below to check on Amazon Website</p>
                    <a href="{self.product_url}">CLICK ME!!</a>
                </div>
            </body>
        </html>
        """

        # part1 = MIMEText(email_body, "plain")
        part2 = MIMEText(email_link, "html")  # Attach the html as a html text to the email body

        # new_message.attach(part1)
        new_message.attach(part2)
        with open(r"image/price_down_alert.png", "rb") as image_data:
            msgImage = MIMEImage(image_data.read())
        msgImage.add_header("Content-ID", "<image1>")
        new_message.attach(msgImage)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="ricky.kristianb@gmail.com",
                msg=new_message.as_string()
            )
