def generate_series(x:int):
    res = []
    if(x % 2 == 0):
        x = x-1
    for i in range(1, x+1):
        res.append(2*i - 1)
    return res


if __name__ == "__main__":
    x = int(input("Enter a number: "))
    series = generate_series(x)
    print("Result: ",", ".join(map(str,series)))