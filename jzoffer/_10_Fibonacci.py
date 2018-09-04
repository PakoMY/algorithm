#斐波那契数列返回第n项
def fibonacci(n):
    pre = 1
    current = 1
    if n <= 0:
        return False
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            container = current
            current = current + pre
            pre = container
        return current
