import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Tolerance for stopping the series (1e-15 for 10 decimal places accuracy)
tol = 1e-15

# Initialize the series sum
series_sum = mp.mpf(0)

# Start at m=0
m = 0

# Compute the first term (m=0)
current_term = mp.mpf(1) / 3  # term for m=0

# Loop until the term becomes smaller than the tolerance
while abs(current_term) >= tol:
    # Add the current term to the series sum
    series_sum += current_term
    
    # Move to the next m
    m += 1
    
    # Calculate the recurrence factor for the next term
    # Factor = [(2m)(2m-1)] / [(2m+1) * (m^2) * 36]
    numerator = (2 * m) * (2 * m - 1)
    denominator = (2 * m + 1) * (m ** 2) * 36
    factor = numerator / denominator
    
    # Compute the next term using the recurrence relation
    current_term *= factor

# Multiply the series sum by pi to get the final result
result = mp.pi * series_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))