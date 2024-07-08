import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    
    numbers_set = set()
    while len(numbers_set) < quantity:
        number = random.randint(min, max)
        numbers_set.add(number)
    
    numbers_list = sorted(list(numbers_set))
    
    return numbers_list

print(get_numbers_ticket(1, 49, 6)) 
print(get_numbers_ticket(1, 36, 5)) 
print(get_numbers_ticket(1, 1000, 10))
