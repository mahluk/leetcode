import sys

def calculate(expression):
  operands = []
  operators = []
  result = 0

  for term in expression:
    # number
    if term.isnumeric():
      if operators != []:
        top_operator = operators[len(operators) - 1]
      else:
        top_operator = ""

      # division and multiplication
      if top_operator in ['/', '*']:
        operation = operators.pop()

        if operation == '/':
          operands.append(operands.pop() // int(term))
        else:
          operands.append(operands.pop() * int(term))
      # sum and substraction
      else:
        operands.append(int(term))
    elif term != ' ' :
      operators.append(term)

  print(operators)
  print(operands)
  while operators != []:
    operation = operators.pop()
    if operation == '-':
      result -= operands.pop()
    else:
      result += operands.pop()

  return result + operands.pop()

if __name__ == "__main__":
  print(calculate(sys.argv[1]))
