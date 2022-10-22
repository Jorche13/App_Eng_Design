import time
from weather import *
#default time for running the pump in seconds
water_time = 10

#default moisture threshold
threshold_moisture = 45

#value for testing 
dummy_value = 30

def waternow(timer):

    print("Hermano Manuex riega tus plantas! Manuex es genial")

def run():


    while(1):

        b = DataPoint()
        if decide(b) == True:
            #the code decided that water is needed, water the plants
            waternow(water_time)   
        else:
            print("Your plants are moist <3")
        
        #make thread sleep for five minutes 
        time.sleep(5)


#deciding wheter plants need water
def decide(b: DataPoint):
    current_moisture = dummy_value
    rain_val = b.get_rain_three_hours()
    temp_val = b.get_temp()

    if current_moisture < 45:
        if rain_val < 0.7:
            waternow(water_time)
    else:
        if temp_val > 30:
            if rain_val < 0.7 and current_moisture < 60:
                waternow(water_time)
            




    
