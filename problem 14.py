def compute():
    # Cache to store Collatz chain lengths for previously computed numbers
    cache = {1: 1}
    max_length = 1
    result = 1

    # Iterate over all starting numbers under 1 million
    for i in range(2, 1_000_000):
        n = i
        steps = 0

        # Follow the Collatz sequence until we reach a cached value
        while n not in cache:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            steps += 1

        # Total chain length is the steps taken plus the known length from cache
        total_length = steps + cache[n]

        # Store the result for the current starting number
        cache[i] = total_length

        # Update the maximum if this sequence is the longest so far
        if total_length > max_length:
            max_length = total_length
            result = i

    return str(result)

if __name__ == "__main__":
    print(compute())