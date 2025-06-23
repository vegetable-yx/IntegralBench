import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 3^(1/4)
three_power = mp.power(3, 0.25)

# Calculate error functions at 3^(1/4)
erf_term = mp.erf(three_power)
erfi_term = mp.erfi(three_power)
sum_error_functions = erf_term + erfi_term

# Calculate sqrt(2) constant
sqrt_two = mp.sqrt(2)

# Combine all components
result = sqrt_two * three_power * mp.pi * sum_error_functions

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))