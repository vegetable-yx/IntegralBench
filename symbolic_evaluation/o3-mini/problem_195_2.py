import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the value of pi divided by 2
pi_over_2 = mp.pi / 2

# Subtract pi/2 from 2 to get the result
result = 2 - pi_over_2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))