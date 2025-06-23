import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 32 to get the result
result = pi_squared / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))