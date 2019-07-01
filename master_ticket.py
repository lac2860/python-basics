SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

#create the calculate_price function. It takes number of tickets and returns
#num_tickets *Tocket_price
def calculate_price(tickets):
    service_charge = SERVICE_CHARGE * tickets
    return tickets * TICKET_PRICE + SERVICE_CHARGE
    

#Run this code continuosly until ticket run out

while tickets_remaining:
    
    
    # Output how many tickets are remaining using the tickets_remaining variable
    
    print("There are {} tickets remaining.".format(tickets_remaining))
          
          
    #Gather the user's name ans assign it to a new varialble
          
    name = input("What is your name? ")
          
    #Promp the user by name and ask how many yickets they would like 
    try:      
        tickets = input("Hello {}, How many tickets would you like? ".format(name))
        #Expect a ValueError to happen and handle it appropriately.
        #valid number no more than 100
        tickets = int(tickets)
        
        if tickets > tickets_remaining:
        
            raise ValueError("There are only {} tickets remaining" .format(tickets_remaining ))
    except ValueError as err:
        print("We ran into an issue. {}. Please try again".format(err))
        
    else:      
    # Calculate the price (number of tickets multiplied by the price and assign it to avariable
              
        total_price_tickets = calculate_price(tickets)
              
        # Output the price to the screEN
          
        print("The total price would be ${}".format(total_price_tickets))
        
        #Promp user if they want to proceed. y/n?
        
        
        should_proceed=input("Would you like to proceed Y/N? ")
        
        
        #IF they want to proceed
        if should_proceed.lower() == "y" :
            # print out to the screen "SOLD!" to confirm purchase 
            #TODO: Gather credit card information and process it.
            
            print("SOLD")
        
            #and then decrement the tickets remaining by the number of tickets purchase
            tickets_remaining -=  tickets
        #Otherwise..
        else:
            print("Thank you, {}".format(name))
            print("The total price would be {}".format(total_price_tickets))
            #thank them
        
    #notify there are no more tickets
print("Sorry the tickets are all sold out!!")
