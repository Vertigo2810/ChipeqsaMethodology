import requests
import colorama
from colorama import Fore
import os
import random 
import sys
from time import sleep
import fade
import concurrent.futures
import pyfiglet


figlet = pyfiglet.figlet_format("Chipeqsa Methodology", font = "slant"  )
text = (figlet)
faded_text = fade.brazil(text)
print(faded_text)

colorama.init()

list = ["\033[0;91m[+] Chipeqsa, sheni safulis garanti ! \n ", "\033[0;91m[+] Ginda ayeno palajenia? Gqondes chemtan good atlashenia ! \n ", "\033[0;91m[+] Chipeqsas signalebi, ufaso mara miliardad girebuli ! \n", "\033[0;91m[+] Qalebi usmenen usmenen reps, chipeqsas fani ki shoulobs bevrs ! \n "]

text = "\033[0;91m[+] Shemqmneli, Damwer-Developer Batoni Vertigo"
for x in text:
  sleep(0.02) # In seconds
  sys.stdout.write(x)
  sys.stdout.flush()
print()

text = "\033[0;91m[+] Chipeqsas sheni daxmareba surs, mibadze mas da ishove milioni !"
for x in text:
  sleep(0.02) # In seconds
  sys.stdout.write(x)
  sys.stdout.flush()
print()

money = int(input('''\033[0;37m
[+] Sad ginda fulis dadeba ?

[1] Bileti damawerie
[2] romeli sloti vitamasho ?
[3] JetX/Aviator
[4] Random Slogani Chipeqsasgan
    \n
[Pasuxi : (1-3) ]> '''))

if money == 1:
    text = "\033[0;91m[+] Karoche shedixar ormocda merve yazaxetis ligashi da irchev \n    mesame tamashis 2 kushs, uechveli meitans \n <3    "
    for x in text:
      sleep(0.02) # In seconds
      sys.stdout.write(x)
      sys.stdout.flush()


elif money == 2:
        text = "\033[0;91m[+] Mai aritamasho dzma \n    Magan damaqcia ro movutyan momgoni \n <3    "
        for x in text:
          sleep(0.02) # In seconds
          sys.stdout.write(x)
          sys.stdout.flush()



elif money == 3:
        text = "\033[0;91m[+] Patara mayutit magali X \n   An didi mayutit 1.20 X \n <3    "
        for x in text:
          sleep(0.02) # In seconds
          sys.stdout.write(x)
          sys.stdout.flush()


          
elif money == 4:
        text = random.choice(list)
        for x in text:
          sleep(0.02) # In seconds
          sys.stdout.write(x)
          sys.stdout.flush()

else:
    print("Ar wer sworad dzamia")
