import os
import errno

try:
    os.mkdir("upload/Linuz Tri Erianto")
except OSError as exc:
    if exc.errno != errno.EEXIST:
        print("sini23")
        raise
    os.system("cd upload ; rm -rf '{}'".format("Linuz Tri Erianto"))
    os.mkdir("upload/Linuz Tri Erianto 3")
    print("success")


"""
[IT TODAY'S COMPETITION : HACKTODAY 2021] 
.
Hello, fellas! 
.
HackToday is a cybersecurity competition that challenges its participants to collect as many flags as possible from the problems provided by the committee. 
.
HackToday is now open to High School Student, Undergrad Student, and the General Public.
.
Registration and details can be seen on the IT TODAY 2021 website:

ittoday.id 
ittoday.id 
ittoday.id 

Registration period from 1 June - 1 August 2021
. 

CP HackToday:
Rizal : 0896-4441-7286 (WhatsApp)
Yosar : 0895-3427-44068 (WhatsApp)
Patar : t.me/patarisac (Telegram)
.
Let's show your hacking skills!

“Our technological powers increase, but the side effects and potential hazards also escalate.” — Alvin Toffler.
"""