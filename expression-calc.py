def do_calc(s: str):
    s = s.replace(' ', '')
    n = len(s)
    
    sm = []

    # get first number
    num1 = ''
    i = 0
    while not any([s[i] in '*/+-']) and i < n:
        num1 += s[i]
        i += 1
    num_i = int(num1)
    
    sm.append(num_i)
    
    # start on first operator
    while i < n:
        n_i = 0
        
        operator = s[i]
        i+=1
        
        n_i = i
        num2 = ''
        while n_i < n and not any([s[n_i] in '*/+-']):
            num2 += s[n_i]
            n_i += 1
        num_i2 = int(num2)
        
        if operator == '*':
            sm.append(num_i2 * sm.pop(-1))
        elif operator == '/':
            sm.append(sm.pop(-1) / num_i2)
        elif operator == '+':
            sm.append(num_i2)
        elif operator == '-':
            sm.append(num_i2 * -1)
        
        i += len(num2)

    return sum(sm)

assert(do_calc('12 + 8 * 6 + 2 * 14') == 12 + 8 * 6 + 2 * 14)
assert(do_calc('12 + 8') == 12 + 8)
assert(do_calc('12 / 2') == 12 / 2)
assert(do_calc('12 - 2') == 12 - 2)
assert(do_calc('3 + 12 / 2') == 3 + 12 / 2)
assert(do_calc('3 + 12 / 2 - 7') == 3 + 12 / 2 - 7)
assert(do_calc('15 * 3 + 34 * 16') == 15 * 3 + 34 * 16)
assert(do_calc('2 + 15 * 3 / 4 + 34 * 16') == 2 + 15 * 3 / 4 + 34 * 16)
assert(do_calc('2 + 15 * 3 - 5 / 4 + 34 * 16') == 2 + 15 * 3 - 5 / 4 + 34 * 16)