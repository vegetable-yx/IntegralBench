import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Initialize sum and first term (k=0)
sum_total = mp.mpf(0)
k = 0
term = mp.mpf(1)  # Term for k=0: (-4)^0 / ((0+1)*(2*0+1)!)
sum_total += term

# Tolerance for term magnitude to break loop (1e-25 for 10 decimal safety)
tolerance = mp.mpf('1e-25')

while True:
    k += 1
    # Calculate numerator and denominator for current k
    numerator = (-4) ** k
    denominator = (k + 1) * mp.fac(2 * k + 1)
    term = numerator / denominator
    
    sum_total += term
    
    # Check if term is smaller than tolerance
    if mp.fabs(term) < tolerance:
        break

# Multiply by 1/2 as per the original expression
result = sum_total * 0.5

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))