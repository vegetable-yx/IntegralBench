import mpmath as mp

# Set decimal precision for internal calculations
mp.dps = 15

# Compute the first group: ζ(4, 1/2) + ζ(4, 3/2)
zeta4_half = mp.zeta(4, mp.mpf(1)/2)
zeta4_3halves = mp.zeta(4, mp.mpf(3)/2)
group1 = zeta4_half + zeta4_3halves

# Compute the second group: ζ(4, 3/4) + ζ(4, 5/4)
zeta4_3quarters = mp.zeta(4, mp.mpf(3)/4)
zeta4_5quarters = mp.zeta(4, mp.mpf(5)/4)
group2 = zeta4_3quarters + zeta4_5quarters

# Combine the groups with their coefficients
result = 24 * group1 - 3 * group2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))