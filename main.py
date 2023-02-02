from jikanpy import Jikan
import smtplib
import emails
from email.mime.text import MIMEText

jikan = Jikan()
seasonal_anime = jikan.seasons(2023, 'winter')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(emails.sender_email, emails.sender_password)

anime_data = ''
for anime in seasonal_anime["data"]:
    anime_data += anime['title'] + '\n'

msg = MIMEText(anime_data)
msg['Subject'] = 'Seasonal Anime Data'
msg['From'] = emails.sender_email
msg['To'] = emails.recipient_email

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(emails.sender_email, emails.sender_password)
server.send_message(msg)
server.quit()
