'''
Temperature
'''
def c_to_units(temperature, to_unit):
    '''
    convert temperature from c to others units
    '''
    if to_unit == "k":
        temperature = temperature + 273.15
    elif to_unit == "f":
        temperature = (temperature * (9 / 5)) + 32
    else:   # to_unit is "r"
        temperature = (temperature + 273.15) * (9/5)
    return temperature

def f_to_units(temperature, to_unit):
    '''
    convert temperature from f to others units
    '''
    if to_unit == "k":
        temperature = ((temperature - 32) * 5/9) + 273.15
    elif to_unit == "c":
        temperature = (temperature - 32) * 5/9
    else:   # to_unit is "r"
        temperature = temperature + 459.67
    return temperature

def k_to_units(temperature, to_unit):
    '''
    convert temperature from k others units
    '''
    if to_unit == "c":
        temperature = temperature - 273.15
    elif to_unit == "f":
        temperature = ((temperature - 273.15) * 9/5) + 32
    else:   # to_unit is "r"
        temperature = temperature * 9/5
    return temperature

def r_to_units(temperature, to_unit):
    '''
    convert temperature from r to others units
    '''
    if to_unit == "c":
        temperature = (temperature - 491.67) * 5/9
    elif to_unit == "f":
        temperature = temperature - 459.67
    else:   # to_unit is "k"
        temperature = temperature * (5/9)
    return temperature

def temperature_conversion(temperature, from_unit, to_unit):
    '''
    convert temperature to desired unit
    '''
    if from_unit == to_unit:
        return temperature

    match from_unit:
        case "c":
            return c_to_units(temperature, to_unit)
        case "f":
            return f_to_units(temperature, to_unit)
        case "k":
            return k_to_units(temperature, to_unit)
        case "r":
            return r_to_units(temperature, to_unit)

def main():
    '''
    main
    '''
    temperature_in = float(input())
    from_unit = input().lower().strip()
    to_unit = input().lower().strip()

    coverted_temperature = temperature_conversion(temperature_in, from_unit, to_unit)
    print(f"{coverted_temperature:.2f}")
if __name__ == "__main__":
    main()
