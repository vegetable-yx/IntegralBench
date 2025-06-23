import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the cube of pi
pi_cubed = mp.pi ** 3

# Divide by 32 to obtain the result
result = pi_cubed / 32

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))