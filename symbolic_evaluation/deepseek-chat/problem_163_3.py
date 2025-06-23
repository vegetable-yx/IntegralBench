import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ζ(3, 0.25) using Hurwitz zeta function
term1 = mp.zeta(3, mp.mpf('0.25'))

# Compute ζ(3, 0.75) using Hurwitz zeta function
term2 = mp.zeta(3, mp.mpf('0.75'))

# Calculate the difference: ζ(3, 0.25) - ζ(3, 0.75)
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))