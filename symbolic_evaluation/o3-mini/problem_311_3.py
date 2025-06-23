import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate common constant e^{1/4}
exp_term = mp.exp(0.25)

# Compute the Exponential Integral Ei(-1/4)
ei_term = mp.ei(-0.25)

# Compute the complementary error function erfc(1/2)
erfc_term = mp.erfc(0.5)

# Compute the hypergeometric function 2F1(-1/2, 1/2; 3/2; 1/4)
hyp2f1_term = mp.hyp2f1(-0.5, 0.5, 1.5, 0.25)

# Calculate each term of the expression
term1 = -4 * exp_term * ei_term
term2 = 2 * mp.sqrt(mp.pi) * exp_term * erfc_term
term3 = 3 * hyp2f1_term
term4 = -3

# Combine terms and divide by 24
result = (term1 + term2 + term3 + term4) / 24

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))