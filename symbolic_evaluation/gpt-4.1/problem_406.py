import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute constants
sqrt2 = mp.sqrt(2)  # Square root of 2
three_power_1_4 = mp.root(3, 4)  # 3^(1/4)
three_power_minus_1_4 = 1 / three_power_1_4  # 3^(-1/4)

# Compute each argument for arctan functions
arg1 = sqrt2 * three_power_1_4 + 1
arg2 = sqrt2 * three_power_minus_1_4 + 1
arg3 = sqrt2 * three_power_1_4 - 1
arg4 = sqrt2 * three_power_minus_1_4 - 1

# Compute each arctan term
term1 = mp.atan(arg1)  # arctan(sqrt(2)*3^(1/4) + 1
term2 = mp.atan(arg2)  # arctan(sqrt(2)*3^(-1/4) + 1
term3 = mp.atan(arg3)  # arctan(sqrt(2)*3^(1/4) - 1
term4 = mp.atan(arg4)  # arctan(sqrt(2)*3^(-1/4) - 1

# Combine terms according to the expression
result = term1 - term2 + term3 - term4

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))