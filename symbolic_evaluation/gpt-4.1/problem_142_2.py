import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize the sum
k = 0  # Start with k=0
tolerance = mp.mpf('1e-15')  # Tolerance to stop summation when terms are negligible

# Precompute constants outside the loop for efficiency
sqrt_pi_over_2 = mp.sqrt(mp.pi) / 2
four = mp.mpf(4)  # Convert 4 to mpmath type

while True:
    fact_k = mp.factorial(k)  # Calculate k!
    denominator1 = fact_k ** 2 * (2 * k + 1)  # Denominator of the first fraction
    numerator1 = four ** k  # 4^k term
    fraction1 = numerator1 / denominator1  # First part of the term
    
    gamma_k_3_2 = mp.gamma(k + mp.mpf('1.5'))  # Gamma(k + 3/2)
    fraction2 = fact_k / gamma_k_3_2  # Second part of the term
    
    term = sqrt_pi_over_2 * fraction1 * fraction2  # Combine all components
    sum_result += term  # Add the term to the total sum
    
    if mp.fabs(term) < tolerance:  # Check if the term is below the tolerance
        break
    k += 1  # Move to the next term in the series

print(mp.nstr(sum_result, n=10))  # Print the result with 10 decimal places