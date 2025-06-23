import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute ζ(3, 1/4) using Hurwitz zeta function
term1 = mp.zeta(3, 0.25)

# Compute ζ(3, 3/4) using Hurwitz zeta function
term2 = mp.zeta(3, 0.75)

# Calculate the difference between the two terms
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))