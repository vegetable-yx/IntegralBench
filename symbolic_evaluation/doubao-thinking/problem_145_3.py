import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize sum to 0 with mpmath precision
n = 0  # Sum terms until they become smaller than 1e-15
while True:
    numerator = mp.power(4, n)  # Calculate 4^n using mpmath power
    factorial_term = mp.factorial(2*n + 1)  # Compute (2n+1)! using mpmath
    denominator = (n + 1) * (2*n + 1) * factorial_term  # Combine denominator components
    term = numerator / denominator  # Compute current term
    
    sum_result += term  # Add current term to the sum
    
    # Check if term is below precision threshold
    if mp.fabs(term) < mp.mpf('1e-15'):
        break
    
    n += 1  # Increment n for next term

# Print result formatted to exactly 10 decimal places
print(mp.nstr(sum_result, n=10))