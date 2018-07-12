import matplotlib.pyplot as plt
import numpy as np

def matrixToText(m):
    return '\n'.join([' | '.join(t) for t in m])

def printMatrix(m):
    print(matrixToText(m))

def matrixToCsv(m, separator=','):
    return '\n'.join([separator.join(t) for t in m])

def main():
    encoding = 'utf-8'
    data_file_name = 'vest_unb_2018_2_1_chamada_extra_processado.csv'
    data_file = open(data_file_name, 'r', encoding=encoding)
    data_matrix = [line.strip('\n').split(',') for line in data_file.readlines()]
    data_file.close()

    #printMatrix(data_matrix)

    starting_letters_data = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
    for line in data_matrix:
        starting_letters_data[line[0][0]] += 1
    
    #print(starting_letters_data)
    aux1 = list(starting_letters_data.items())
    aux1.sort(key=lambda t:t[1],reverse=True)
    names, values = zip(*aux1)

    plt.figure(1)

    #plt.subplot(131)
    plt.bar(names, values)

    plt.show()

if __name__ == '__main__':
    main()