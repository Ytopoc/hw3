import random
def get_numbers_ticket(umin, umax, quantity):
    lottery_set =set()
    raznitsa= umax-umin +1
    if umin < 1 or umin >= umax or umax > 1000 or quantity < 1 or quantity > raznitsa:
        print( "Не вірні дані" ) 
        return list(lottery_set) 
    else:
        while not quantity == len(lottery_set):
            lottery_set.add(random.randint(umin , umax))
        lottery_numbers= sorted(list(lottery_set))
            
        return sorted(lottery_numbers)
print(get_numbers_ticket(10, 14, 5))
print(get_numbers_ticket(1, 10, 10))




    
          

       
       
      
