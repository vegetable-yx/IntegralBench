import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Cube the value of pi
pi_cubed = pi_val ** 3

# Divide the cubed pi by 12
result = pi_cubed / 12

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))