def generate_hexadecimal_mapping():
    for i in range(99):
        hex_value = format(i, 'x')
        print(f"{i} = 0x{hex_value}")

generate_hexadecimal_mapping()