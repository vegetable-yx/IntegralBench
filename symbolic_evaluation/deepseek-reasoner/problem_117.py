import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^4 using intermediate steps
pi = mp.pi
pi_squared = mp.power(pi, 2)  # Compute π²
pi_fourth = mp.power(pi_squared, 2)  # Compute π⁴ by squaring π²

# Calculate the final result (7π⁴)/256
numerator = mp.fmul(7, pi_fourth)  # Multiply 7 by π⁴
result = mp.fdiv(numerator, 256)  # Divide by 256 to get final value

print(mp.nstr(result, n=10))  # Print result with 10 decimal places