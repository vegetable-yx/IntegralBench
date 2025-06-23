import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (set to example values 1 and 1)
a = 1
b = 1

# Prefactor: sqrt(2 * pi * a) / 2
prefactor = mp.sqrt(2 * mp.pi * a) / 2

# Base for the series: (b * a / 2)
base_val = b * a / 2
base_val_sq = base_val**2  # Precompute (b*a/2)^2 for recurrence

# Initialize the series sum with n=0 term
gamma_num_n0 = mp.gamma(0.25)  # Gamma(n+1/4) at n=0
gamma_den_n0 = mp.gamma(1.75)  # Gamma(n+7/4) at n=0
current_term = gamma_num_n0 / gamma_den_n0
series_sum = current_term

# Set tolerance and maximum terms for convergence
tolerance = 1e-15
max_terms = 1000
n = 1

# Sum the series from n=1 to infinity using recurrence
while n < max_terms:
    # Compute recurrence factor: [(n - 0.75) * (b*a/2)^2] / [(n + 0.75) * (2n) * (2n-1)]
    numerator = (n - 0.75) * base_val_sq
    denominator = (n + 0.75) * (2*n) * (2*n - 1)
    recurrence_factor = numerator / denominator
    
    # Update current term using recurrence
    current_term *= recurrence_factor
    series_sum += current_term
    
    # Check for convergence (if term is below tolerance)
    if mp.fabs(current_term) < tolerance:
        break
    n += 1

# Multiply the series sum by the prefactor to get final result
result = prefactor * series_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))