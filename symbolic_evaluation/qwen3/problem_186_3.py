import mpmath as mp

# Set the decimal places of precision to 15 for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 32
result = pi_squared / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))