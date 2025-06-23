import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate exponential integrals
ei_e = mp.ei(mp.e)  # Exponential integral at e
ei_1 = mp.ei(1)     # Exponential integral at 1

# Calculate exponential terms
exp_term = mp.exp(mp.e - 1)  # e^(e-1)
e_constant = mp.e            # Euler's number

# Combine all components
result = (2 * ei_e) - (2 * ei_1) + exp_term - e_constant

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))