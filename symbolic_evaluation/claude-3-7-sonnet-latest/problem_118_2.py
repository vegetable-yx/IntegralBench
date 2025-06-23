import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi to the power of 3
pi_cubed = mp.power(mp.pi, 3)

# Divide the result by 8
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))