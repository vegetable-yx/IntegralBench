import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameters for the hypergeometric functions
a = [mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf('0.5')]  # numerator parameters: 1/2, 1/2, 1/2
b = [1, mp.mpf('1.5')]  # denominator parameters: 1, 3/2

# Evaluate the first hypergeometric function at z = 1/16
term1 = mp.hyper(a, b, mp.mpf('1')/16)

# Evaluate the second hypergeometric function at z = -1/16
term2 = mp.hyper(a, b, mp.mpf('-1')/16)

# Compute the difference between the two hypergeometric terms
diff = term1 - term2

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))