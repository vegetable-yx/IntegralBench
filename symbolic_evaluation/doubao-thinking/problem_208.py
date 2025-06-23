import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate pi to the fourth power
pi_power4 = pi_squared ** 2

# Compute the final result by dividing by 768
result = pi_power4 / 768

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))