import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute e^{-1/4} using mpmath's exp function
exp_term = mp.exp(-0.25)

# Compute the square root of pi using mpmath's sqrt and pi constant
sqrt_pi = mp.sqrt(mp.pi)

# Multiply the two terms and then by 2
result = 2 * exp_term * sqrt_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))