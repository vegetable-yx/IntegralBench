import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the value of pi using mpmath constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide pi squared by 6 to get the result
result = pi_squared / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))