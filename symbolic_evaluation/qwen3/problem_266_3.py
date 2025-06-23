import mpmath as mp

mp.dps = 15  # Set internal precision

result = mp.mpf(0)
m = 0

# Calculate initial term for m=0
numerator = (-1)**m * 4**m
denominator = (m + 1) * (2*m + 1)**2 * mp.factorial(2*m)
term = numerator / denominator

# Iterate until term magnitude drops below precision threshold
while mp.fabs(term) > 1e-15:
    result += term
    m += 1
    
    # Calculate components for next term
    numerator = (-1)**m * 4**m
    denominator = (m + 1) * (2*m + 1)**2 * mp.factorial(2*m)
    term = numerator / denominator

print(mp.nstr(result, n=10))