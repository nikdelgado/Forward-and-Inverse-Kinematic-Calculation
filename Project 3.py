# Author: Nikolas Delgado
# Class: CS 2300
# Assignment: Program 3
# Description: this program reads in a text file of theta values or coordinates and calculates the forward and inverse kinematic.

import math

def get_data():
	
	# Open and store file data
	f = open("config.txt", "r")
	contents = f.readlines()
	f.close()
	
	# Define and clean link length values
	link_lengths = contents[0]
	link_lengths = link_lengths.split(',')
	
	# Get and clean theta values data set
	theta_vals = contents[5:10]
	
	for i in range(len(theta_vals)):
		theta_vals[i] = theta_vals[i].replace("f: ", "")
		theta_vals[i] = theta_vals[i].replace("\n", "")
		theta_vals[i] = theta_vals[i].split(',')
		
		
	for i in range(len(theta_vals)):
		theta_vals[i][0] = float(theta_vals[i][0])
		theta_vals[i][1] = float(theta_vals[i][1])


#	# Get and clean position values
	pos_vals = contents[1:5]

	for i in range(len(pos_vals)):
		pos_vals[i] = pos_vals[i].replace("i: ", "")
		pos_vals[i] = pos_vals[i].replace("\n", "")
		pos_vals[i] = pos_vals[i].split(',')

	for i in range(len(pos_vals)):
		pos_vals[i][0] = float(pos_vals[i][0])
		pos_vals[i][1] = float(pos_vals[i][1])
		
		
	return link_lengths, theta_vals, pos_vals

def calc_forward_kinematic(link_lengths, theta_vals):
	
	# define l values
	l1 = float(link_lengths[0])
	l2 = float(link_lengths[1])
	
	print("----- Forward Kinematic Calculations ----")
	
	# loop through theta values and calculate x and y values for each
	for i in range(len(theta_vals)):
		x = l2 * math.cos(theta_vals[i][0] + theta_vals[i][1]) + l1 * math.cos(theta_vals[i][0])
		y = l2 * math.sin(theta_vals[i][0] + theta_vals[i][1]) + l1 * math.sin(theta_vals[i][0])
		
		x = round(x, 2)
		y = round(y, 2)
		print(theta_vals[i][0], theta_vals[i][1], " --->", "(",x,",", y, ")")

	return
	
def calc_inverse_kinematic(link_lengths, pos_vals):
	
	print("\n----- Inverse Kinematic Calculations ----")
	
	# Define L values
	l1 = float(link_lengths[0])
	l2 = float(link_lengths[1])
	
	
	# Loop through position values and calculate q2 and q1
	for i in range(len(pos_vals)):
		
		if (pos_vals[i][0] == 0 and pos_vals[i][1] == 0):
			print(pos_vals[i][0], pos_vals[i][1], "---> Position Cannot Be Achieved")
			continue
		
		q2_numerator = (pos_vals[i][0]**2) + (pos_vals[i][1]**2) - ((l1**2) + (l2**2))
		q2_denominator = 2 * (l1 * l2)
		
		try:
			q2 = round(math.acos(q2_numerator / q2_denominator), 5)
		except:
			print(pos_vals[i][0], pos_vals[i][1], "---> Position Cannot Be Achieved")
			continue
			
		try:
			q1_left_side = math.atan2(pos_vals[i][1], pos_vals[i][0])
			val1 = (l2 * math.sin(q2))
			val2 = (l1 + (l2 * math.cos(q2)))
			q1_right_side = math.atan2(val1, val2)
			q1 = q1_left_side - q1_right_side
			q1 = round(q1, 5)

		except:
			print(pos_vals[i][0], pos_vals[i][1], "---> Position Cannot Be Achieved")
			continue
		
		print(pos_vals[i][0], pos_vals[i][1], "--->", "(", q1,",", q2, ")")
		
	return

	
def main():
	link_lengths, theta_vals, pos_vals = get_data()

	calc_inverse_kinematic(link_lengths, pos_vals)	
	calc_forward_kinematic(link_lengths, theta_vals)

	
main()