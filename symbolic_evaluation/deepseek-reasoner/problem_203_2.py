import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
j0 = mp.besselj(0, 1)

# Calculate Bessel function of the first kind of order 1 at 1
j1 = mp.besselj(1, 1)

# Sum the Bessel function values
sum_bessel = j0 + j1

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * sum_bessel

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))