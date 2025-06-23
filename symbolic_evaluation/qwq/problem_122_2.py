import mpmath as mp
# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the calculated pi
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 4 to get final result
result = mp.fdiv(pi_squared, 4)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))