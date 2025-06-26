def generate_odd_series(x:int):
    res = []
    for i in range(1, x+1):
        res.append(2*i - 1)
    return res

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    series = generate_odd_series(x)
    print("Result: ", ", ".join(map(str,series)))
