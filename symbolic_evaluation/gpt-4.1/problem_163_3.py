import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the first part: 8 * [ζ(3, 1/2) - ζ(3, 3/2)]
# Calculate ζ(3, 1/2)
zeta_3_half = mp.zeta(3, mp.mpf(1)/2)

# Calculate ζ(3, 3/2)
zeta_3_threehalf = mp.zeta(3, mp.mpf(3)/2)

# Compute the difference for the first part
diff1 = zeta_3_half - zeta_3_threehalf
term1 = 8 * diff1

# Compute the second part: [ζ(3, 1/4) - ζ(3, 5/4)]
# Calculate ζ(3, 1/4)
zeta_3_quarter = mp.zeta(3, mp.mpf(1)/4)

# Calculate ζ(3, 5/4)
zeta_3_fivequarter = mp.zeta(3, mp.mpf(5)/4)

# Compute the difference for the second part
diff2 = zeta_3_quarter - zeta_3_fivequarter

# Combine both terms: term1 - diff2
result = term1 - diff2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))