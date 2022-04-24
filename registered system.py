from smtplib import SMTP
print("STUDENT REGİSTRETİON SYSTEM")
print("")
print("=======MENU=======")
print("")
print("1) Add New Student İnfirmation")
print("2) View Registered İnformation")
email=print("3) Send İnformation to E-mail")
print("")
while True:
    choice=input("Make your Choice(1/2/3):")
    if choice=="1":
        a=input("Enter Student's Name:")
        b=input("Enter Student's Age:")
        if len(a and b)<=0:
            print("Please do not leave blank")
            continue
        else:
            print("Student information added")
            skip=input("Do you want to continue(Y/N):")
            if skip=="e":
                print("REGİSTERED İNFORMATİON")
                print("Student name:",a,"Student age:",b)
                continue
            if skip=="h":
                break;
    
    if choice=="2":
        print("Student name:",a,"Student age:",b)
        skip2=input("Do you want to continue(Y/N):")
        if skip2=="e":
            continue
        else:
            break;
    if choice=="3":
        # Mail content
        subject = "Student registered system"
        message = "Student name:",a,"Student age:",b
        content = "Subject: {0} \n {1}".format(subject,message)
        # Mail Account İnformation
        myMailAdress = "yourmail@gmail.com"
        password = "your_mail_password"
        # Who to send information to
        sendTo = "whosend@gmail.com"
        mail = SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, subject.encode("utf-8"))
        print("Successfully sent")
        break;
        
                    




        


   
