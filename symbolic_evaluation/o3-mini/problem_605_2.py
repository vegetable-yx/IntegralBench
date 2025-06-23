import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi (π) using mpmath's constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 16 to get the result
result = pi_squared / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))