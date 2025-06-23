import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Compute pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 16 to obtain the result
result = pi_squared / 16

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))