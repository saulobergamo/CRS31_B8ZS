import matplotlib.pyplot as plt

def convert_to_b8zs(binary_sequence):
    b8zs_code = ""
    b8zs_graph = []

    count_zeros = 0
    last_one = -1

    for bit in binary_sequence:
        if bit == '0':
            count_zeros += 1
            b8zs_graph.append(0)
            b8zs_code += '0'

            if count_zeros == 8:
                b8zs_graph.reverse()
                for i in range (8):
                    b8zs_graph.remove(0)
                    b8zs_code = b8zs_code[:-1]
                
                b8zs_graph.reverse()
                b8zs_graph += [0, 0, 0, last_one, -1*last_one, 0, -1*last_one ,last_one]
                # b8zs_code -= '00000000'
                b8zs_code += '000VB0VB'

        else:  # bit == '1'
            b8zs_code += '1'
            last_one *= -1
            b8zs_graph += [1*last_one]
            count_zeros = 0

    return b8zs_code, b8zs_graph

# Plotting
def plot_b8zs(b8zs_graph):
    plt.plot(b8zs_graph, drawstyle='steps-pre')
    plt.title('Gráfico do Código de Linha B8ZS')
    plt.show()


