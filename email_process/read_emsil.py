email_path="email_process\\email.txt"

gmail_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\email_process\\gmail.txt"

yahoo_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\email_process\\yahoo.txt"

outlook_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\email_process\\outlook.txt"

fr_email=open(email_path,"r")
fw_gmail=open(gmail_path,"w")
fw_yahoo=open(yahoo_path,"w")
fw_outlook=open(outlook_path,"w")

for line in fr_email:

    mail_id=line.strip("\n")

    if mail_id.endswith("gmail.com"):

        fw_gmail.write(mail_id+"\n")

    elif mail_id.endswith("yahoo.com"):

        fw_yahoo.write(mail_id+"\n")

    elif mail_id.endswith("outlook.com"):

        fw_outlook.write(mail_id+"\n")


print("program end")


