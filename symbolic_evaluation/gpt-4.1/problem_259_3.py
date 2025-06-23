import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2 * sin(1)
sin_value = mp.sin(1)
doubled_sin = 2 * sin_value

# Calculate 2 * Si(1) using the sine integral function
si_value = mp.si(1)
doubled_si = 2 * si_value

# Combine results: 2*sin(1) - 2*Si(1)
result = doubled_sin - doubled_si

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))