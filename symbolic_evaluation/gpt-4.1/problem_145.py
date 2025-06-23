import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter 'a' (adjust as needed)
a = 1.0

# Precompute constants
sqrt_pi = mp.sqrt(mp.pi)  # sqrt(π)
const_factor = a * sqrt_pi / 4  # Constant factor: (a * sqrt(π)) / 4
base = (a ** 2) / 4  # Base for the power term: a^2 / 4

# Initialize the series sum
series_sum = mp.mpf(0)
k = 0
# Tolerance for stopping the series when terms become negligible
tol = mp.mpf('1e-30')  # Using a tolerance smaller than 1e-15 for safety

# Sum the series until terms are below tolerance
while True:
    # Compute factorial term: (k+1)!
    fact_term = mp.factorial(k + 1)
    
    # Compute denominator term: (2k+1)
    linear_term = 2 * k + 1
    
    # Compute Gamma(k + 3/2) = Gamma(k + 1.5)
    gamma_term = mp.gamma(k + 1.5)
    
    # Compute denominator: (k+1)! * (2k+1) * Gamma(k+1.5)
    denominator = fact_term * linear_term * gamma_term
    
    # Compute the power term: (a^2/4)^k
    power_term = base ** k
    
    # Compute current series term: power_term / denominator
    term = power_term / denominator
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence: stop if term is below tolerance
    if mp.fabs(term) < tol:
        break
    
    # Increment k for the next term
    k += 1

# Multiply the series sum by the constant factor to get the final result
result = const_factor * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))