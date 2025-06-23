import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Dawson function value at 1
dawson_value = mp.dawsn(1)

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * dawson_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))