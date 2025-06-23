import mpmath as mp

# Set the internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the numerator: 19 * π
numerator = mp.mpf(19) * mp.pi

# Compute the result by dividing the numerator by 512
result = numerator / mp.mpf(512)

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))