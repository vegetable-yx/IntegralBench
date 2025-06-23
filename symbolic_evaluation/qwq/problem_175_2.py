import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Cube the value of pi
pi_cubed = pi_value ** 3

# Divide the cubed pi by 96
result = pi_cubed / 96

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))