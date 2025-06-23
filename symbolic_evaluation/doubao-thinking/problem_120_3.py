import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi^4
pi_power4 = mp.pi ** 4

# Divide by 32 to get the final result
result = pi_power4 / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))