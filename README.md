# Anime Data Retrieval and Sharing Tool
A python script that grabs seasonal anime data using [Jikan API](https://jikan.moe/) and emails it to you.

![image](https://github.com/AjwadIbnSwalehin/Jikan-API-Project/assets/103510865/b9bb9a3d-0ef5-4759-a1f0-2dd1b73ccca1)

## Requirements
You'll need the following to be able to run this:
- `jikanpy`
- `smtplib`
- `emails`

To install the libraries run:
```
pip3 install jikanpy
```
Replace jikanpy with smtplib as well. With emails, create a separate file called emails.py and enter in the following code:
```python
sender_email = "Enter email address you want to send with"
sender_password = "Enter email address's password"
recipient_email = "Enter recipient's email address"
```

## Usage
Before using the script, please change the following code on line 8 in `main.py` to match your needs
```python
seasonal_anime = jikan.seasons(2023, 'winter') # Change year and season as necessary
```

Run `main.py` on any Python IDE and you should receive an email.
