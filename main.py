from jikanpy import Jikan
import smtplib
import emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

jikan = Jikan()
seasonal_anime = jikan.seasons(2023, 'winter')

server = smtplib.SMTP('smtp.gmail.com', 25)
server.starttls()
server.login(emails.sender_email, emails.sender_password)

msg = MIMEMultipart()
msg['Subject'] = 'Seasonal Anime Data'
msg['From'] = emails.sender_email
msg['To'] = emails.recipient_email

text_template = "<h2>{}</h2>"

anime_data = "<html><head></head><body>"
for anime in seasonal_anime["data"]:
    text = text_template.format(anime["title"])
    image_url = anime["images"]["jpg"]["large_image_url"]
    synopsis = anime["synopsis"]
    anime_data += "<p>{}<br><img src='{}'></p>".format(text, image_url)

anime_data += "</body></html>"

text = MIMEText(anime_data, 'html')
msg.attach(text)

server.ehlo()
server.login(emails.sender_email, emails.sender_password)
server.send_message(msg)
server.quit()
