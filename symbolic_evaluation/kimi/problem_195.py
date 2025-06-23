import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide pi squared by 4
term1 = pi_sq / 4

# Divide pi by 2
term2 = mp.pi / 2

# Subtract term2 from term1
result = term1 - term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))