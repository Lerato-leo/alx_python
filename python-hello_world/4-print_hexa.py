def numbers():
    for i in range(99):
        return f"{i} = {hex(i)}"

print(numbers())