import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate trigamma function at 1/4
term1 = mp.polygamma(1, mp.mpf(1)/4)

# Calculate trigamma function at 3/4
term2 = mp.polygamma(1, mp.mpf(3)/4)

# Compute the difference: ψ^(1)(1/4) - ψ^(1)(3/4)
diff = term1 - term2

# Multiply by 1/8
result = diff / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))