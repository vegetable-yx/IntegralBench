import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi/4 using mpmath's pi constant
pi_value = mp.pi
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))