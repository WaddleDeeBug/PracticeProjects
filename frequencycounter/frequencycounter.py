def frequency_counter(data_list):
    # Create an empty dictionary to store the frequencies
    frequency_dict = {}

    # Loop through the list and update the frequencies
    for item in data_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    # Return the frequency dictionary
    return frequency_dict

# Ask the user to input a list of items separated by commas
user_input = input("Enter items separated by commas (e.g., apple,banana,apple): ").lower()

# Convert the input string into a list
input_list = [item.strip() for item in user_input.split(",")]

# Call the frequency_counter function
result = frequency_counter(input_list)

# Display the result
print("Frequencies:", result)