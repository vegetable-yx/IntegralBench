import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 2 to get the result
result = pi_squared / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))