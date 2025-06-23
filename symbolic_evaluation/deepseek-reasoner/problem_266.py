import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

a = mp.mpf(1)  # Define the value of 'a' (adjust as needed)

sum_part = mp.mpf(0)  # Initialize the summation part
k = 0
term = mp.mpf(1)  # Initialize the first term (k=0)

while True:
    # Calculate current term components
    sign = (-1) ** k
    a_power = a ** (2 * k)
    denominator = (k + 1) * (2 * k + 1) ** 2 * mp.factorial(2 * k)
    
    current_term = (sign * a_power) / denominator
    sum_part += current_term
    
    # Check if term is below precision threshold
    if mp.fabs(current_term) < 1e-15:
        break
    
    k += 1

# Multiply by a/2 to get final result
result = (a / 2) * sum_part

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))