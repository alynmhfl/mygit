# 1. Take the number of points one team is ahead. 
points_str = input("Enter the lead in points: ") 
points_remaining_int = int(points_str) 

# 2. Subtract three. 
lead_calculation_float= float(points_remaining_int - 3) 

# 3. Add a half—point if the team that is ahead has the ball, 
# and subtract a half—point if the other team has the ball. 
has_ball_str = input("Does the lead team have the ball (Yes or No): ") 

if has_ball_str == 'Yes': 
<<<<<<< HEAD
	lead_calculation_float= lead_calculation_float + 0.5 
else: 
  	lead_calculation_float= lead_calculation_float - 0.5 
=======
lead_calculation_float= lead_calculation_float + 0.5 
else: 
  lead_calculation_float= lead_calculation_float - 0.5 
>>>>>>> 18c914b4c2cd114c891bbe7e2bf1cd7639d196e5

# (Numbers less than zero become zero) 
if lead_calculation_float< 0: 
	lead_calculation_float= 0 

# 4. Square that. 
lead_calculation_float= lead_calculation_float** 2 
# 5. If the result is greater than the number of seconds left in the game, the lead is safe . 
seconds_remaining_int = int(input("Enter the number of seconds remaining: ")) 

if lead_calculation_float> seconds_remaining_int: 
<<<<<<< HEAD
  	print("Lead is safe.") 
else: 
  	print("Lead is not safe.") 
=======
  print("Lead is safe.") 
else: 
  print("Lead is not safe.") 
>>>>>>> 18c914b4c2cd114c891bbe7e2bf1cd7639d196e5

