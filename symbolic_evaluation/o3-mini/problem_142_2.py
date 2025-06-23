import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (example value, can be modified)
a = mp.mpf('1.0')

# Maximum number of terms to prevent infinite loops
max_m = 10000
# Tolerance for term magnitude to break the loop
tol = mp.mpf('1e-25')

# Initialize sum and starting index
s = mp.mpf(0)
m = 0
# First term in the series (m=0)
term = mp.mpf(1)

# Sum the series until tolerance or max_m is reached
while m < max_m and abs(term) > tol:
    # Add current term to the sum
    s += term
    
    # Increment m for the next term
    m += 1
    
    # Calculate the next term using recurrence relation:
    # term_{m} = term_{m-1} * (a^2 / 4) / (m^2) * (2m-1)/(2m+1)
    term = term * (a**2 / 4) / (m**2) * (2*m - 1) / (2*m + 1)

# Print the result to 10 decimal places
print(mp.nstr(s, n=10))