import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Define the argument for the hypergeometric functions
z_val = mp.mpf(1)/16

# Compute the first hypergeometric function: _2F_1(-1/2, 1/2; 3/2; 1/16)
hyp1 = mp.hyp2f1(mp.mpf('-0.5'), mp.mpf('0.5'), mp.mpf('1.5'), z_val)

# Compute the second hypergeometric function: _2F_1(-1/2, 1/2; 5/2; 1/16)
hyp2 = mp.hyp2f1(mp.mpf('-0.5'), mp.mpf('0.5'), mp.mpf('2.5'), z_val)

# First term: π times the first hypergeometric function
term1 = mp.pi * hyp1

# Second term: 2 times the second hypergeometric function
term2 = 2 * hyp2

# Compute the difference: term1 - term2
diff = term1 - term2

# Multiply by 1/64 to get the final result
result = diff / 64

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))