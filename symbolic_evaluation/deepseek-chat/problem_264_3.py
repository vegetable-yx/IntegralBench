import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Bessel function J0 at 1
j0_1 = mp.besselj(0, 1)

# Square the Bessel function value
j0_sq = j0_1**2

# Calculate the expression: (pi/4) * (1 - J0(1)^2)
result = (mp.pi / 4) * (1 - j0_sq)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))