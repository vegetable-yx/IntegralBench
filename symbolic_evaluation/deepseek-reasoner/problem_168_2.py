import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Cube the value of pi
pi_cubed = pi_value ** 3

# Divide the cubed pi by 8 to get the final result
result = pi_cubed / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))