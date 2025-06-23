import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide pi squared by 2
pi_sq_over_2 = pi_sq / 2

# Compute complete elliptic integral of the first kind at k=0.5
K_val = mp.ellipk(0.5)

# Square the elliptic integral value
K_sq = K_val ** 2

# Multiply squared elliptic integral by 2
two_K_sq = 2 * K_sq

# Compute final result: π²/2 - 2*[K(0.5)]²
result = pi_sq_over_2 - two_K_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))