import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the components of the argument for arcsin
sqrt3 = mp.sqrt(3)  # Compute square root of 3
numerator = sqrt3 - 1  # Calculate numerator of the arcsin argument
argument = numerator / 2  # Final argument for arcsin function

# Compute the arcsin and final result
arcsin_value = mp.asin(argument)  # Calculate inverse sine of the argument
result = 2 * arcsin_value  # Multiply by 2 as per formula

print(mp.nstr(result, n=10))  # Print result with 10 decimal places precision