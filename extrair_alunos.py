import tabula

def matrixToText(m):
    return '\n'.join([' | '.join(t) for t in m])

def printMatrix(m):
    print(matrixToText(m))

def matrixToCsv(m, separator=','):
    return '\n'.join([separator.join(t) for t in m])

def main():
    folder_path = 'C:\\Users\\caac\\Desktop\\teste\\'
    nao_processado = 'vest_unb_2018_2_1_chamada_cru.csv'
    processado = 'vest_unb_2018_2_1_chamada.csv'
    #tabula.convert_into(folder_path+'ED_13_2018_VEST_UNB_18_2_1___CHAMADA.PDF', folder_path+nao_processado, output_format='csv', pages='all')
    
    header = ['Nome do Candidato', 'Numero de inscricao', 'Numero do documento de identidade', 'Curso / Turno / Campus']
    accepted_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    accepted_letters += [chr(i) for i in range(ord('a'), ord('z')+1)]
    accepted_letters += [chr(i) for i in range(ord('0'), ord('9')+1)]
    accepted_letters += ['Ã', 'Á', 'À', 'Â', 'É', 'Ê', 'Í', 'Õ', 'Ó', 'Ô', 'Ú', 'Ç', 'ã', 'á', 'à', 'â', 'é', 'ê', 'í', 'õ', 'ó', 'ô', 'ú', 'ç']
    accepted_letters += [' ', '-', '(', ')', '/', ',', '\n']
    #print(accepted_letters)

    targetEncoding = 'utf-8'

    csv = open(nao_processado, 'r')
    matrix = []
    num = 0
    num2 = 0
    for line in csv.readlines():
        if num2 < 5:
            num2 += 1
        else:
            aux = ''.join([letter for letter in line if letter in accepted_letters])
            splitted = aux.replace('\n','').split(',')
            #print(splitted)
            if splitted[0] == '' or splitted[1] == '' or splitted[2] == '' or splitted[3] == '':
                aux = [matrix[num-1][i]+' '+splitted[i] for i in range(1,4)]
                aux.insert(0, matrix[num-1][0])
                matrix[num-1] = aux
            else:
                matrix.append(splitted)
                num += 1
    matrix.insert(0, header)
    csv.close()

    new_csv = open(processado, 'w', encoding=targetEncoding)
    new_csv.write(matrixToCsv(matrix))
    new_csv.close()

    altered_matrix = [[l[0], l[1], l[2]]+[t.strip(' ') for t in l[3].rsplit('/', 2)] for l in matrix]
    printMatrix(altered_matrix[:3])
    new_csv = open(processado.replace('.csv', '_extra_processado.csv'), 'w', encoding=targetEncoding)
    new_csv.write(matrixToCsv(altered_matrix))
    new_csv.close()

    cursos = sorted(set([l[3].strip(' ') for l in matrix]))
    n = 0
    for curso in cursos:
        aprovados = [l for l in matrix if curso == l[3].strip(' ')]
        aprovados.insert(0, header)
        new_csv = open('cursos\\'+processado.replace('.csv', curso+'.csv').replace('/', '-').replace(' ',''), 'w', encoding=targetEncoding)
        new_csv.write(matrixToCsv(aprovados))
        new_csv.close()

if __name__ == "__main__":
    main()