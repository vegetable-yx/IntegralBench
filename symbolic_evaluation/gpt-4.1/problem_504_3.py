import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Choose a value for x (arbitrary, since not specified; user can modify as needed)
x = 0.5

# Precompute constants
n = 99
power2_100 = mp.power(2, 100)  # 2^100
total_sum = mp.mpf(0)           # Initialize sum

# Loop over j from 0 to 99 inclusive
for j in range(0, 100):
    # Calculate binomial coefficient C(99, j)
    binom_val = mp.binomial(n, j)
    
    # Compute term1: sin(2(1+j)x) / (2(1+j))
    a = 1 + j
    term1 = mp.sin(2 * a * x) / (2 * a)
    
    # Compute term2: sin(2(100-j)x) / (2(100-j))
    b = 100 - j
    term2 = mp.sin(2 * b * x) / (2 * b)
    
    # Add binomial coefficient multiplied by (term1 - term2) to the total sum
    total_sum += binom_val * (term1 - term2)

# Multiply the sum by 1/2^100 (and set constant C=0)
result = total_sum / power2_100

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))