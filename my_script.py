def fibonacci(n):
    """Generate a Fibonacci sequence of length n."""
    sequence = [0, 1]
    
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
        
    return sequence

print("Fibonacci sequence up to 10:")
result = fibonacci(10)
print(result)
