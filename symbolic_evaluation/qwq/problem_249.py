import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 for intermediate calculations

# Calculate components of the expression step by step
sqrt_5 = mp.sqrt(5)  # Compute square root of 5
half_sqrt5 = sqrt_5 / 2  # Divide by 2
subtracted_term = half_sqrt5 - 1  # Subtract 1 from the result
result = mp.pi * subtracted_term  # Multiply by π

print(mp.nstr(result, n=10))  # Print result with 10 decimal places