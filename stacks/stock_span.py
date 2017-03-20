def span(C):
    stack, top = [0], -1
    result = [1]
    for i, x in enumerate(C[1:], start=1):
        while len(stack) > 0 and x >= C[stack[top]]:
            stack.pop()

        if len(stack) == 0:
            result.append(i + 1)
        else:
            result.append(i - stack[top])

        stack.append(i)
    return result


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# price = [10, 4, 5, 90, 120, 80]
price = [10, 6, 4, 5, 90, 120, 80]
n = len(price)
