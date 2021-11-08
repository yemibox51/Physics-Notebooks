#!/usr/bin/env python3

'''Procedure A
def wavelength_desc(l, anti_nodes):
	total = (2 * l)/anti_nodes
	total = total * 40
	print(total)
	
	
tension = [1.176, 1.372, 1.568, 1.764]
anti_nodes = [7, 5, 6]

length_of_string = 1.76

wavelength = [.503, .704, .587]

frequency1 = [40, 30, 35]
frequency2 = [45, 32, 39]
frequency3 = [50, 30, 42]
frequency4 = [55, 38, 46]

for i in range(0, len(wavelength)):
	#wavelength_desc(length_of_string, anti_nodes[i])
	total = round(frequency1[i] * wavelength[i], 2)
	#print(total)
	
'''
# Procedure B

frequency = [1000, 950, 900, 850, 800] #hz

#in cm
'''
one = [7.20, 4.0, 5.81, 8.30, 8.00]
two = [26.10, 22.30, 25.30, 28.31, 29.20]
three = [41.54, 41.20, 44.12, 48.50, 51.90]
four = [58.53, 58.31, 63.10, 68.71, 74.00]
'''
one = [.0720, .040, .0581, .0830, .0800]
two = [.2610, .2230, .2530, .2831, .2920]
three = [.4154, .4120, .4412, .4850, .5190]
four = [.5853, .5831, .6310, .6871, .7400]

delta = [None] * 5 #m
v = [None] * 5 #m/s
total = [None] * 5
for i in range(0, len(frequency)):
	total[i] = round((2/5) * (one[i] + (2 * two[i]) + (3 * three[i]) + (4 * four[i]) ) - (one[i] + (two[i]) + (three[i]) + (four[i]) ), 4)
	
print(total)	