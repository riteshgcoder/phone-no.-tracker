import phonenumbers
from phonenumbers import geocoder
phone_numbers1=phonenumbers.parse("+918115201618")
phone_numbers2=phonenumbers.parse("+4930901820")
phone_numbers3=phonenumbers.parse("+6564746474")
print(geocoder.description_for_number(phone_numbers1,"en"))
print(geocoder.description_for_number(phone_numbers2,"en"))
print(geocoder.description_for_number(phone_numbers3,"en"))

OUTPUT:-
C:\visual code>python -u "c:\visual code\phone number.py"
India
Berlin
Singapore
