import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the constant pi divided by 2
pi_over_2 = mp.pi / 2

# Subtract pi_over_2 from 2
result = 2 - pi_over_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))