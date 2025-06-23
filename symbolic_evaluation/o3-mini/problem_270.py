import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the hypergeometric function: _2F_1(1/2, 1; 7/2; 1/4)
hyp2f1_val = mp.hyp2f1(0.5, 1, 3.5, 0.25)

# Compute pi and its powers
pi = mp.pi
pi_sq = pi**2
pi_cubed = pi**3

# Calculate the term: 96 * pi * (2 - pi) * hyp2f1_val
term = 96 * pi * (2 - pi) * hyp2f1_val

# Compute the numerator: -15*pi^3 + 120*pi^2 - 256 + term
numerator = -15 * pi_cubed + 120 * pi_sq - 256 + term

# Denominator is 4608
denominator = 4608

# Final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))