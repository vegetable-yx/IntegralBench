import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the components step by step
sqrt3 = mp.sqrt(3)  # Compute square root of 3
numerator = sqrt3 - 1  # Calculate numerator of the arcsin argument
argument = numerator / 2  # Compute the argument for arcsin
arcsin_value = mp.asin(argument)  # Calculate arcsin of the argument
result = 2 * arcsin_value  # Multiply by 2 as per the original expression

print(mp.nstr(result, n=10))  # Print result with 10 decimal places