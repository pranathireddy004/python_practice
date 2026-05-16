#move all the zeros to end in py

# Move all zeros to the end of the list
# Keep the order of non-zero elements the same

numbers = [0, 1, 0, 3, 12]

# Two-pointer approach
j = 0  # position where next non-zero should be placed

for i in range(len(numbers)):
    if numbers[i] != 0:
        # Swap current non-zero with the element at index j
        numbers[j], numbers[i] = numbers[i], numbers[j]
        j += 1

print(numbers)   # Output: [1, 3, 12, 0, 0]