import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi/12 using mpmath's constant for pi
pi_value = mp.pi
result = pi_value / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))