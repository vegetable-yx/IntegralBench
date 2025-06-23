import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate e^2
e_squared = mp.exp(2)

# Calculate 1/e^2
inv_e_squared = 1 / e_squared

# Calculate the term (1 - 1/e^2)
term = 1 - inv_e_squared

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))