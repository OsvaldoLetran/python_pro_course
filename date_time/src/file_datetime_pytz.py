from datetime import datetime
import pytz

my_city_timezone = pytz.timezone('America/Bogota')
my_city_time = datetime.now(my_city_timezone)
print("Bogotá: ", my_city_time.strftime("%d/ %m/ %Y, %H: %M: %S"))


my_city_timezone = pytz.timezone('America/Mexico_City')
my_city_time = datetime.now(my_city_timezone)
print("Ciudad de Mexico: ", my_city_time.strftime("%d/ %m/ %Y, %H: %M: %S"))