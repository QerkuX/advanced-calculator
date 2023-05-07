def isSymbol(char):
    symbols = ['+', '-', '*', '/']

    for symbol in symbols:
        if char == symbol:
            return True
    return False

def decodeInput(text):
    symbolPos = [0]
    nums = []
    for char in range(1, len(text)-1):
        if isSymbol(text[char]):
            if text[char] == '-' and symbolPos[-1] == char:
                continue
            nums.append(float(text[symbolPos[-1] : char]))
            symbolPos.append(char+1)
    

    if len(symbolPos) == 1:
        print("hi")
        return False
    
    symbolPos.pop(0)

    try:
        nums.append(float(text[symbolPos[-1] : len(text)]))
    except ValueError:
        return False
    
    symbols = []
    for pos in symbolPos:
        symbols.append(text[pos-1])

    return [nums, symbols]

def hierarchy(symbols):
    symbolPos = [[],[]]
    score = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }

    for symbol in range(len(symbols)):
        symbolPos[score[symbols[symbol]]].append(symbol)

    return symbolPos[1] + symbolPos[0]



def calc(nums, symbols):
    ans = 0
    order = hierarchy(symbols)
    for symbol in order:
        match(symbols[symbol]):
            case '+':
                ans = nums[symbol] + nums[symbol+1]
            case '-':
                ans = nums[symbol] - nums[symbol+1]
            case '*':
                ans = nums[symbol] * nums[symbol+1]
            case '/':
                if nums[symbol+1] == 0:
                    ans = 0
                else:
                    ans = nums[symbol] / nums[symbol+1]

        nums.pop(symbol+1)
        nums[symbol] = ans
        symbols.pop(symbol)
        for pos in range(len(order)):
            if symbol < order[pos]:
                order[pos] -= 1

    return ans

def checkInput(text):
    decoded = decodeInput(text)
    if decoded:
        return decoded
    print("Wrong input (format: [number][symbol][number] | example: 123+456)")
    return False

def start():
    print("format: [number][symbol][number] | example: 123+456\n")
    decoded = False
    while True:
        decoded = checkInput(input())
        if decoded:
            break

    loop(calc(decoded[0], decoded[1]))
    

def loop(placeholder):
    decoded = False
    while True:
        decoded = checkInput(str(placeholder) + input(placeholder))
        if decoded:
            break

    loop(calc(decoded[0], decoded[1]))

start()
