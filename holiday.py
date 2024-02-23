
"""

@author: mattmeadows
"""

# Program to develop a costing for a typical holiday.

# Asks for an input for flight destination.

# Asks for length of stay and days needed for a rental car.

# Uses pre-determined costs for each input choice

# Calculates total cost of holiday taking in flight cost and daily cost of stay and car rent multiplied by users input for length.

city_flight = input(" What city are you looking to fly to? Popular destinations include: London, Paris, Rome and Madrid. " + " \n ")

num_nights = input(" How many nights would you like to stay for? " + " \n ")

rental_days = input(" How many days would you like to rent a car for? " + " \n ")


def hotel_cost(num_nights):
    
    one_night = 150
    
    num_cost = int(num_nights) * one_night
    
    return num_cost

print("")
print("-"*60)   
print("") 
print("The cost of your hotel stay will be: " + " £ " + str(hotel_cost(num_nights)))



def plane_cost(city_flight):
    
    if city_flight.upper() == "LONDON":
        flight_cost = 125
        
    elif city_flight.upper() == "PARIS":
        flight_cost = 100
        
    elif city_flight.upper() == "MADRID":
        flight_cost = 80
        
    elif city_flight.upper() == "ROME":
        flight_cost = 75
        
    else:
        flight_cost = 60
        
    return flight_cost

print("")    
print("The cost of your flight will be: " + " £ " + str(plane_cost(city_flight)))  


    
def car_rental(rental_days):
    
    one_rental_day = 60
    
    rental_cost = int(rental_days) * one_rental_day
    
    return rental_cost

print("")
print("The total cost of renting a car will  be: " + " £ " + str(car_rental(rental_days)))    




def holiday_cost(hotel_cost, plane_cost, car_rental):
    
    total_cost = int(hotel_cost(num_nights)) + int(plane_cost(city_flight)) + int(car_rental(rental_days))
    
    return total_cost

print("")
print("-"*60)
print("")
print("The total cost of your holiday will be: " + " £ " + str(holiday_cost(hotel_cost, plane_cost, car_rental)))
   
    

