input_file = open("./input", "r")
all_fuel = 0
all_fff = 0
fuel = 0


for mass in input_file.readlines():
    mass = int(mass.strip("\n"))
    
    fuel = mass // 3 - 2
    
    fuel_for_fuel = 0
    rest_fuel = fuel // 3 - 2
    while rest_fuel > 0:
        fuel_for_fuel += rest_fuel
        rest_fuel = rest_fuel // 3 - 2


    all_fff += fuel_for_fuel
    all_fuel += fuel
input_file.close()
print("fuel needed for rocket: ", all_fuel)
print("fuel needed for fuel:   ", all_fff)
print("total fuel consumtion:  ", all_fuel + all_fff)
