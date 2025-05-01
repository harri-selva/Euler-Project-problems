def compute():
    total_length = 0
    for i in range(1, 1001):
        total_length += get_number_word_length(i)
    return str(total_length)


def get_number_word_length(n):
    # Handle numbers 1-19 directly (simple lookup in ONES)
    if 1 <= n < 20:
        return len(ONES[n])

    # Handle numbers 20-99 (combination of TENS and ONES)
    elif 20 <= n < 100:
        return len(TENS[n // 10]) + (len(ONES[n % 10]) if n % 10 != 0 else 0)

    # Handle numbers 100-999 (hundreds + TENS/ONES)
    elif 100 <= n < 1000:
        length = len(ONES[n // 100]) + len("hundred")
        if n % 100 != 0:
            length += len("and") + get_number_word_length(n % 100)
        return length

    # Handle 1000
    elif n == 1000:
        return len("one") + len("thousand")

    return 0


# Words for the numbers from 0 to 19
ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# Words for the tens (20, 30, 40, ..., 90)
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


if __name__ == "__main__":
    print(compute())