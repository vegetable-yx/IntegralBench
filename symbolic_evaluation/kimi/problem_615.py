import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute s = inverse hyperbolic sine of 7
s = mp.asinh(7)

# Compute the terms involving hyperbolic cosine
term1 = (mp.mpf(3)/4) * mp.cosh(4 * s / 3)
term2 = (mp.mpf(3)/2) * mp.cosh(2 * s / 3)

# Calculate the upper limit contribution
upper = term1 - term2

# Calculate the lower limit contribution (t=0)
lower = (mp.mpf(3)/4) * mp.cosh(0) - (mp.mpf(3)/2) * mp.cosh(0)

# Compute the final result by subtracting lower from upper
result = upper - lower

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))