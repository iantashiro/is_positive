import math
import importlib

def get_roman(num):
    v = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    s = ['(M)', '(CM)', '(D)', '(CD)', '(C)', '(XC)', '(L)', '(XL)', '(X)', '(IX)', '(V)', '(IV)', 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    res = ""; n = num
    for i in range(len(v)):
        count = n // v[i]; res += s[i] * count; n -= v[i] * count
    return res

def is_positive(n):
    if n <= 0: return False
    
    roman_val = get_roman(math.ceil(n))
    final_result = False 
    
    for i in range(10):
        module_name = f"check_{i}"
        try:
            shard = importlib.import_module(module_name)
            if shard.check(roman_val):
                final_result = True 
        except ImportError:
            continue
            
    return final_result 