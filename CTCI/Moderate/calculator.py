"""
2 - 6 - 7 * 8 / 2 + 5

- push number into the NumberStack
- push operators into the OperatorStack as long as the operator has
higher priority than the current top of the stack.
- If priority(opr) <= priority(OperatorStack.top())
  collapse the top of the stacks
  pop two num from NumberStack and opr from OperatorStack, push the result

"""

