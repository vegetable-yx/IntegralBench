import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Initialize the sum and term variables
total = mp.mpf(0)  # Holds the cumulative sum of the series
k = 0              # Current index in the series
term = mp.mpf(1)   # Starting term for k=0: 1/(4^0 * 1 * 1 * (0!)^2) = 1

# Tolerance for termination: stop when term < 1e-15
tolerance = mp.mpf('1e-15')

# Compute the series sum using recurrence to avoid recalculating factorials
while True:
    total += term   # Add current term to the total
    k += 1          # Move to next index
    
    # Calculate the recurrence factor for next term:
    # term_{k} = term_{k-1} * (2k-1) / [4 * k * (k+1) * (2k+1)]
    numerator = mp.mpf(2*k - 1)
    denominator = mp.mpf(4 * k * (k+1) * (2*k+1))
    factor = numerator / denominator
    
    # Update term for next iteration
    term = term * factor
    
    # Break loop if next term is below tolerance
    if abs(term) < tolerance:
        break

# Multiply the series sum by π^3 / 8
pi_cubed = mp.pi ** 3
result = (pi_cubed / 8) * total

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))