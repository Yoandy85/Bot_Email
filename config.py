import os 
radr = os.environ["BOTEMAIL"]  # direccion a utilizar para el bot
pwd = os.environ["PASS"] # contraseña base64.b64encode
admin = os.environ["MIEMAIL"] # direccion de quien administra el bot
imapserver = "imap.gmail.com"  # servidor imap
smtpserver = "smtp.gmail.com"  # servidor smtp
smtpserverport = 587  # puerto tls smtp
check_freq = 15 #Frecuencia con la q se revisa la bandeja