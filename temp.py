# code to take input temperature in celcius, fahrenheit, or kelvin and convert to the other two temperatures
# this assumes that the first input is a number of degrees and the second input gives the units
# ex: run temp.py 32 f
#
import numpy as np
import sys

val = sys.argv[1]
let = sys.argv[2]
print(val, let)

if let in ['K', 'k']:
    kel = np.float(val)
    cel = kel - 273.
    fah = cel * 9. / 5. + 32
    print('the temperature of '+str(kel)+' Kelvin corresponds to ...')
    print(str(cel)+' degrees Celsius and')
    print(str(fah)+' degrees Fahrenheit')

if let in ['C', 'c']:
    cel = np.float(val)
    kel = cel + 273.
    fah = cel * 9. / 5. + 32
    print('the temperature of '+str(cel)+' Celcius corresponds to ...')
    print(str(kel)+' degrees Kelvin and')
    print(str(fah)+' degrees Fahrenheit')

if let in ['F', 'f']:
    fah = np.float(val)
    cel = (fah - 32.) * 5. / 9.
    kel = cel + 273.
    print('the temperature of '+str(fah)+' Fahrenheit corresponds to ...')
    print(str(cel)+' degrees Celcius and')
    print(str(kel)+' degrees Kelvin')
    
