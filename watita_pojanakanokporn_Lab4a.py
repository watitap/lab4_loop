# Imperial to Metric Converter

attempts = 0 # condition primer

# Vars
KILOMETERS = 1.6
LITERS = 3.9
KILOMETERS = 0.45
CENTIMETERS = 2.54


# converting Miles to Kilometers
while attempts < 3: # Check how many invalid numbers have been given
    miles_to_kilometers = float(input("\nPlease tell me how many miles you want converted to kilometers: "))
    
    if miles_to_kilometers < 0:
        print("You cannot enter a negative number, please enter again. \n")
        attempts += 1
    else:
        attempts = 0
        break
        
# Converting Gallons to liters
while attempts < 3: # Check how many invalid numbers have been given
    gallons_to_liters = float(input("\nPlease tell me how many gallons you want converted to liters: "))
    
    if gallons_to_liters < 0:
        print("You cannot enter a negative number, please enter again later. \n")
        attempts += 1
    else:
        attempts = 0
        break
                
# Converting Pounds to Kilograms 
while attempts < 3: # Check how many invalid numbers have been given
    pounds_to_kilograms = float(input("\nPlease tell me how many pounds you want converted to kilograms: "))

    if pounds_to_kilograms < 0:
        print("You cannot enter a negative number, please enter again later. \n")
        attempts += 1
    else:
        attempts = 0
        break

# Converting Inches to Centimeters
while attempts < 3: # Check how many invalid numbers have been given
    inches_centimeters = float(input("\nPlease tell me how many inches you want converted to centimeters: "))
    
    if inches_centimeters < 0:
        print("You cannot enter a negative number, please enter again later. \n")
        attempts += 1
    else:
        attempts = 0 
        break

# Converting Fahrenheit to Celsius
while attempts < 3: # Check how many invalid numbers have been given
    fahrenheit_to_celsius = float(input("\nPlease tell me how many fahrenheit you want converted to celsius: "))
    CELSIUS = (fahrenheit_to_celsius - 32) * 5 / 9
    if fahrenheit_to_celsius > 1000:
        print("You cannot enter number higher than 1,000, please enter again later. \n")
        attempts += 1
    else:
        break

if attempts >=3:
    print("Too many invalid numbers. Program has been terminated.")

if attempts < 3:
    
    print("\n", miles_to_kilometers, " miles is equal to ", 
          format(miles_to_kilometers * KILOMETERS,'.2f'), " kilometers.", sep ='')
    
    print(gallons_to_liters, " gallons is equal to ", 
          format(gallons_to_liters * LITERS,'.2f'), " liters.", sep ='')
    
    print(pounds_to_kilograms, " pounds is equal to ", 
          format(pounds_to_kilograms * KILOMETERS,'.2f'), " kilograms.", sep ='')
    
    print(inches_centimeters, " inches is equal to ", 
          format(inches_centimeters * CENTIMETERS, '.2f'), " centimeters.", sep ='')
    
    print(fahrenheit_to_celsius, " fahrenheit is equal to ", 
          format(CELSIUS, '.2f'), " celsius.", sep ='')  
