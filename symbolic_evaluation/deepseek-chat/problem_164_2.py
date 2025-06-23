import mpmath as mp

# Set internal precision to 15 decimal places for accurate results
mp.dps = 15

# Calculate each term of the expression using the Hurwitz zeta function
# Term1: 4 * ζ(4, 0.5)
term1 = 4 * mp.zeta(4, 0.5)

# Term2: 4 * ζ(4, 1.5)
term2 = 4 * mp.zeta(4, 1.5)

# Term3: (1/2) * ζ(4, 0.75)
term3 = 0.5 * mp.zeta(4, 0.75)

# Term4: (1/2) * ζ(4, 1.25)
term4 = 0.5 * mp.zeta(4, 1.25)

# Combine terms: 4ζ(4,0.5) + 4ζ(4,1.5) - ζ(4,0.75)/2 - ζ(4,1.25)/2
inner_sum = term1 + term2 - term3 - term4

# Multiply by the outer coefficient 6
result = 6 * inner_sum

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))