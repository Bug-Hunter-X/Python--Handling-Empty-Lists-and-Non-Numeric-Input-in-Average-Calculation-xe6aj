def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        print("Error: List contains non-numeric values.")
        return None

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 30, 40, 50.5]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 