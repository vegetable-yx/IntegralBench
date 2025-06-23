import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute first term: 8[ζ(3,1/2) - ζ(3,3/2)]
# ζ(3,1/2) - Hurwitz zeta at s=3, a=1/2
zeta1 = mp.zeta(3, mp.mpf('0.5'))
# ζ(3,3/2) - Hurwitz zeta at s=3, a=3/2
zeta2 = mp.zeta(3, mp.mpf('1.5'))
diff1 = zeta1 - zeta2
term1 = 8 * diff1

# Compute second term: [ζ(3,3/4) - ζ(3,5/4)]
# ζ(3,3/4) - Hurwitz zeta at s=3, a=3/4
zeta3 = mp.zeta(3, mp.mpf('0.75'))
# ζ(3,5/4) - Hurwitz zeta at s=3, a=5/4
zeta4 = mp.zeta(3, mp.mpf('1.25'))
diff2 = zeta3 - zeta4
term2 = diff2

# Combine terms: term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))