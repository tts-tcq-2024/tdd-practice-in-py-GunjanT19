def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]
    
    # Handle new line separators
    numbers = numbers.replace("\n", delimiter)
    
    # Split numbers by the delimiter and calculate the sum
    num_list = numbers.split(delimiter)
    
    negatives = []
    sum = 0
    for num in num_list:
        num_int = int(num)
        if num_int < 0:
            negatives.append(num_int)
        elif num_int <= 1000:
            sum += num_int
    
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return sum

