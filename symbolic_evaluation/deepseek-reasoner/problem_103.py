import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Divide by 12 to get the final result
result = pi_squared / 12

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))