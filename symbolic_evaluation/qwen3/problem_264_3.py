import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind of order 0 at 1
j0 = mp.besselj(0, 1)

# Square the Bessel function result
j0_squared = j0 ** 2

# Calculate the term (1 - J0(1)^2)
term = 1 - j0_squared

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))