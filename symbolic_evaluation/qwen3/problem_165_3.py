import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at x=1
j0_value = mp.besselj(0, 1)

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * j0_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))