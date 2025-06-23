import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi divided by 2
pi_over_2 = mp.pi / 2

# Subtract pi/2 from 1
result = 1 - pi_over_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))