from phonenumbers import geocoder, carrier, timezone
#رساله ترحيبية 
print("   Welcome to the phone data knowledge program \n   BY Muhammad  Alaa " "\n   M.A" )
print ("""
░░█████████
░░▒▀█████▀░
░░▒░░▀█▀
░░▒░░█░
░░▒░█
░░░█
░░█░░░░███████
░██░░░██▓▓███▓██▒
██░░░█▓▓▓▓▓▓▓█▓████
██░░██▓▓▓(◐)▓█▓█▓█
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█
░▒░░▒░░██▓██░░░██▓▓██
████████████████████████
█▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█
██─██▀█─██─██─█─███─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀







""")
#print ("    *" , "\n * " , '  *') , print ("    *" , "\n * " , '  *' ) 
# Enter Your Name 
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
#رساله ترحيبية 
print("   Welcome to the phone data knowledge program \n   BY Muhammad  Alaa " "\n   M.A" )
#print ("    *" , "\n * " , '  *') , print ("    *" , "\n * " , '  *' ) 
# Enter Your Name 
q = str(input("   Enter Your Name : "))
print ("  Welcome "  + q)
#Enter Number 
entered_num = str(input("  Please Enter a Phone Number , Write Numbers Only: "))
#لطبع كود الدولة مع الرقم المدخل
phone_numbers = phonenumbers.parse(entered_num, None)
##لطبع كود الدولة مع الرقم المدخل
print(phone_numbers)
#طبغ معلومات الموقع الجغرافي 
print(geocoder.description_for_number(phone_numbers , "en"))
#معرفه نوع خط الرقم مثلا فودافون  موبايلي  زين ...،
print (carrier.name_for_number(phone_numbers , "ar"))
#طبع المنطقة الذي يوجد بها الرقم
print(timezone.time_zones_for_number(phone_numbers))


#يلزم ادخل مفتاح الدولة قبل كتابه الرقم 
#ا#ذا لم تود ذلك ف ادخل بدلاً من كله 
#None ادخل مكانها كود الدولة التي ترغب في البحث عن الرقم فيها

#The code is editable 

#"en , ar " تعني لغه الكود الذي يظهر لك 
# By Mohammed Alaa 4:05 of the time  2023 / 9 /6 of the dat

#يلزم ادخل مفتاح الدولة قبل كتابه الرقم 
#ا#ذا لم تود ذلك ف ادخل بدلاً من كله 
#None ادخل مكانها كود الدولة التي ترغب في البحث عن الرقم فيها

#The code is editable 

#"en , ar " تعني لغه الكود الذي يظهر لك 
# By Mohammed Alaa 4:05 of the time  2023 / 9 /6 of the date 📅
