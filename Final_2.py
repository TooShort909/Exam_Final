def count_frequencies(strings):
    frequency_count = {}
    for word in strings:
        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1
    return frequency_count

# Example usage
input_strings = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency_count = count_frequencies(input_strings)
print("Frequency Count:", frequency_count)
