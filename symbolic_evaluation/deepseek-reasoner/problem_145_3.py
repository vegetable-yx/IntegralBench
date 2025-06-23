import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel function of the first kind at 1
I0_1 = mp.besseli(0, 1)

# Square the Bessel function result
I0_squared = I0_1 ** 2

# Calculate the term inside the parentheses
term = I0_squared - 1

# Multiply by π/2 to get final result
result = (mp.pi / 2) * term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))