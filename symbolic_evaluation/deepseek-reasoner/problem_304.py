import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the hypergeometric function component
hyp2f1_term = mp.hyp2f1(0.5, 1.5, 3, 0.25)

# Multiply by π and divide by 48
pi_contribution = mp.pi * hyp2f1_term
result = pi_contribution / 48

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))