import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate trigamma function at 1/4
term1 = mp.polygamma(1, mp.mpf(1)/4)

# Calculate trigamma function at 3/4
term2 = mp.polygamma(1, mp.mpf(3)/4)

# Compute the difference between the trigamma values
diff = term1 - term2

# Multiply by 1/8 to get the final result
result = diff / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))