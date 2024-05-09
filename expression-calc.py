def do_calc(s: str):
    s = s.replace(' ', '')
    n = len(s)
    
    md = []
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
            sm.append(num_i2 * (1 / sm.pop(-1)))
        elif operator == '+':
            sm.append(num_i2)
        elif operator == '-':
            sm.append(num_i2 * -1)
        
        i += len(num2)

    return sum(sm)

print(do_calc('12 + 8 * 6 + 2 * 14'))