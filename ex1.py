def count_a(seq):
    """Counting the number of a's in the sequence"""

    # Counter for the A's
    result = 0
    for b in seq:
        if b == 'A':
            result += 1


    # Return the result
    return result


# Main program
s = "AGTACATGGT"
na = count_a(s)
print("The number of A's is: {}" .format(na))

# Calculate the total lenght of the sequence
total_length = len(s)

#Calculate the percentage of A's in the sequence
percentage = round((na/total_length) * 100, 1)

print("The total lenght is: {}" .format(total_length))
print("The percentage of A's is: {}" .format(percentage))




