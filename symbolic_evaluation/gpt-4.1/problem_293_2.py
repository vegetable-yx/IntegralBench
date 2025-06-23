import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)

# Tolerance for breaking the loop (1e-30 is safe for 10 decimal output)
tol = mp.mpf('1e-30')

# We'll iterate until the term becomes smaller than tolerance
n = 0
max_iter = 10000  # high upper bound to prevent infinite loops

while True:
    # Convert current index n to mpmath float
    n_val = mp.mpf(n)
    
    # Calculate the denominator: (n + 3/2) * (n + 1/2)
    denom1 = n_val + mp.mpf('1.5')  # n + 3/2
    denom2 = n_val + mp.mpf('0.5')  # n + 1/2
    denom_product = denom1 * denom2
    
    # Calculate the ratio: (n + 1) / [(n + 3/2)(n + 1/2)]
    ratio = (n_val + 1) / denom_product
    
    # Square the ratio
    ratio_sq = ratio ** 2
    
    # Calculate the geometric factor: (1/4)^n
    geo_factor = (mp.mpf('0.25')) ** n_val
    
    # Compute the term: (π/4) * ratio_sq * geo_factor
    term = (mp.pi / 4) * ratio_sq * geo_factor
    
    # Add term to the sum
    s += term
    
    # Check if the term is below tolerance to break
    if mp.fabs(term) < tol:
        break
    
    # Break if max_iter reached
    if n >= max_iter:
        break
    n += 1

# The result is the computed sum s
result = s

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))