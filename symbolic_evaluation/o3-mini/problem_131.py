import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define the argument for the hypergeometric functions
z = mp.mpf(1)/16

# Compute the first hypergeometric function: 0F1(; 3/2; 1/16)
hyp0f1_32 = mp.hyper([], [mp.mpf(3)/2], z)

# Compute the second hypergeometric function: 0F1(; 5/2; 1/16)
hyp0f1_52 = mp.hyper([], [mp.mpf(5)/2], z)

# Calculate the first term: (π√2 / 2) * 0F1(; 3/2; 1/16)
term1 = (mp.pi * mp.sqrt(2)) / 2 * hyp0f1_32

# Calculate the second term: (1/16) * 0F1(; 5/2; 1/16)
term2 = (1/16) * hyp0f1_52

# Sum the terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))