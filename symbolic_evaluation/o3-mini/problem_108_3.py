import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute gamma(3/4) and square it
gamma_val = mp.gamma(3/4)
gamma_squared = gamma_val**2

# Compute the two hypergeometric functions
hyp1 = mp.hyp2f1(-0.5, 0.25, 0.75, 0.5)  # _2F_1(-1/2, 1/4; 3/4; 1/2)
hyp2 = mp.hyp2f1(0.5, 0.25, 0.75, 0.5)    # _2F_1(1/2, 1/4; 3/4; 1/2)

# Compute the expression inside the brackets: 16 * hyp1 - 7 * hyp2
bracket = 16 * hyp1 - 7 * hyp2

# Compute the denominator: 10 * sqrt(2 * pi)
denominator = 10 * mp.sqrt(2 * mp.pi)

# Combine all parts: [gamma_squared * bracket] / denominator
result = (gamma_squared * bracket) / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))