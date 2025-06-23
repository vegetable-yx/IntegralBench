import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 4: π²/4
pi_sq_over_4 = pi_sq / 4

# Compute complete elliptic integral of the first kind K(m) with m = (1/2)^2 = 1/4
# Note: mp.ellipk(m) corresponds to K(m) where m = k²
elliptic_val = mp.ellipk(0.25)

# Multiply to get final result: (π²/4) * K(1/4)
result = pi_sq_over_4 * elliptic_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))