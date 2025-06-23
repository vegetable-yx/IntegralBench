import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Compute the complete elliptic integral of the first kind at 0.5
k_value = mp.ellipk(0.5)

# Square the elliptic integral value
k_sq = k_value ** 2

# Compute the final result: pi^2 - 2 * (K(0.5))^2
result = pi_sq - 2 * k_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))