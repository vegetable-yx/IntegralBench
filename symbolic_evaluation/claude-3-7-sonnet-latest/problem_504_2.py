import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute the constant factor: -1 / 2^99
constant_factor = -1 / mp.power(2, 99)

# Initialize the summation variable
sum_val = mp.mpf(0)

# Loop over k from 0 to 49 (inclusive)
for k in range(0, 50):
    # Compute the sign: (-1)^(49-k)
    sign = mp.power(-1, 49 - k)
    
    # Compute the binomial coefficient C(99, k)
    binom_coeff = mp.binomial(99, k)
    
    # Compute the denominator (200 - 2k)
    denom = 200 - 2 * k
    
    # Compute the term: sign * binom_coeff / denom
    term = sign * binom_coeff / denom
    
    # Add the term to the sum
    sum_val += term

# Multiply the sum by the constant factor
result = constant_factor * sum_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))