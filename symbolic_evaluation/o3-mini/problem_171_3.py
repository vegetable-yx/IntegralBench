import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the argument for the hypergeometric functions
z = mp.mpf('0.25')

# Calculate the first hypergeometric function: _2F_1(-1/2, 1/2; 3; 1/4)
hyp1 = mp.hyp2f1(mp.mpf('-0.5'), mp.mpf('0.5'), mp.mpf('3'), z)

# Calculate the second hypergeometric function: _2F_1(-1/2, 1/2; 2; 1/4)
hyp2 = mp.hyp2f1(mp.mpf('-0.5'), mp.mpf('0.5'), mp.mpf('2'), z)

# Compute the numerator components
term1 = 16 * hyp1   # 16 times the first hypergeometric function
term2 = 8 * hyp2    # 8 times the second hypergeometric function
term3 = 5 * mp.pi   # 5 times pi
term4 = mp.mpf(8)   # constant 8

# Combine terms to form the numerator: term1 - term2 + term3 - term4
numerator = term1 - term2 + term3 - term4

# Denominator is 2^10 = 1024
denominator = mp.mpf(1024)

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))