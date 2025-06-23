import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the constant pi divided by 2
pi_over_2 = mp.pi / 2

# Subtract pi/2 from 2 to get the result
result = 2 - pi_over_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))