import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate zeta(3, 0.25) - Hurwitz zeta function with s=3, a=0.25
term1 = mp.zeta(3, 0.25)

# Calculate zeta(3, 0.75) - Hurwitz zeta function with s=3, a=0.75
term2 = mp.zeta(3, 0.75)

# Compute the difference between the two terms
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))