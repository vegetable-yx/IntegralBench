import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/2 using mpmath constants
pi_value = mp.pi  # Get the constant π from mpmath
result = pi_value / 2  # Divide π by 2 to obtain the result

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))