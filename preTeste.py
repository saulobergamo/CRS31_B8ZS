import b8zs

def main():
    binary_sequence = '100000000'
    b8zs_code, b8zs_graph = b8zs.convert_to_b8zs(binary_sequence)
    print('Código de linha B8ZS:', b8zs_code)
    b8zs.plot_b8zs(b8zs_graph)

if __name__ == '__main__':
    main()