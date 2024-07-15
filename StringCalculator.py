class StringCalculator:

    def add(self, numbers):
        if numbers == "":
            return 0
        
        # Check for custom delimiter declaration
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_index = numbers.find("\n")
            delimiter = numbers[2:delimiter_index]
            numbers = numbers[delimiter_index + 1:]
        
        # Replace new lines with the delimiter
        numbers = numbers.replace("\n", delimiter)
        
        # Split numbers by the delimiter and convert to integers
        nums = map(int, numbers.split(delimiter))
        
        # Check for negatives
        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
        
        # Ignore numbers greater than 1000
        nums = [num for num in nums if num <= 1000]
        
        # Return the sum of numbers
        return sum(nums)


