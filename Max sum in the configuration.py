def max_sum(a,n):
    total_sum = sum(a)
    current_sum = sum(i * a[i] for i in range(n))
    max_sum_val = current_sum
    
    for i in range(1, n):
        # Compute the new sum based on the previous sum
        current_sum = current_sum + total_sum - n * a[n - i]
        max_sum_val = max(max_sum_val, current_sum)
    
    return max_sum_val
