import random
def get_numbers_ticket(min,max, quantity):
    if min >= 1 and max <=1000 and quantity > 0 and quantity <= max:
        rand_num = range(min,max+1)
        pik = random.sample(rand_num, quantity)
        pik_sorted = sorted(pik)
        print(pik_sorted)
        return pik_sorted 
    else:
        print([])
        return []
    

while True:
    
    try:
        a = int(input("Введіть мінімальне значення: "))
        b = int(input("Введіть максимальне значення: "))
        с = int(input("Введіть бажану кількість генерованих чисел: "))
        get_numbers_ticket(a, b, c)
        break
    except ValueError:
        print("Введіть число")


