import re
def add(var1): 
    if var1 == "" or var1 == "0":
        return 0
    delimiter = delimiter_call(var1)
    var2=numbers(var1,delimiter)
    result=sumnumbers(var2)
    return result
def delimiter_call(var1):
     if var1.startswith("//"):
         return var1[2]
     return ','
def numbers(var1,delimiter):
     if var1.startswith("//"):
         return var1[4:].split(delimiter)
     return re.split(rf"{re.escape(delimiter)}|\n", var1)
def sumnumbers(var2):
    return sum(parse_int(num) for num in var2 if valid_number(num))
def parse_int(num_str):
    try:
        return int(num_str)
    except ValueError:
        return 0
def valid_number(num_str):
    try:
        num=int(num_str)
        return num<=1000
    except ValueError:
        return False
    
   

    
    
    
