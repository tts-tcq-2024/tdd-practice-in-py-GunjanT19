class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            custom_delimiter, numbers = numbers.split("\n", 1)
            delimiter = custom_delimiter[2:]
        
        numbers = numbers.replace("\n", delimiter)
        numbers_list = numbers.split(delimiter)
        
        negatives = [int(num) for num in numbers_list if num.startswith('-')]
        if negatives:
            raise Exception(f"Negatives not allowed: {', '.join(map(str, negatives))}")
        
        return sum(int(num) for num in numbers_list if int(num) <= 1000)
