import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os

def send_email_with_attachment(\
		receiver_email, \
		file_path, \
		sender_email = "polyachenkoya@gmail.com", \
		password=open(os.path.join(os.path.expanduser("~"), 'gmp.dat')).readline()[:-1], \
		subject = "MY_EMAIL_PY", \
		body = "Hi,\n\nPlease find the attached file.\n\nBest regards,\nYury"):
	"""
	Sends an email with an attachment.

	Args:
		receiver_email (str): The recipient's email address.
		file_path (str): The path to the file to attach.
	"""
	# Create the email
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message.attach(MIMEText(body, "plain"))

	# Attach the file
	try:
		with open(file_path, "rb") as attachment:
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header(
			"Content-Disposition",
			f"attachment; filename={file_path.split('/')[-1]}",
		)
		message.attach(part)
	except FileNotFoundError:
		print(f"Error: File {file_path} not found.")
		return

	# Send the email
	try:
		with smtplib.SMTP("smtp.gmail.com", 587) as server:
			server.starttls()  # Secure the connection
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message.as_string())
			print("Email sent successfully!")
	except Exception as e:
		print(f"Error: {e}")

# Example usage:
#send_email_with_attachment("polyachenkoya@princeton.edu", "/home/ypolyach/Downloads/cv_edu.pdf")
