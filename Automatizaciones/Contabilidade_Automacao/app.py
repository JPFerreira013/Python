#entrar na planilha
import openpyxl

#biclioteca para poder copiar com caractere especial
import pyperclip
#biblioteca para poder usar o mouse
import pyautogui

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
#selecionar a sheet correta dentro da planilha
sheet_productos = workbook['Produtos']

#entrar na linha correta da planilha, pulando o titulo das colunas
for coluna in sheet_productos.iter_rows(min_row=2, values_only=True):
    nome_produto = coluna[0]
    pyperclip.copy(nome_produto)
    pyautogui.click(863,72,duration=1)
    pyautogui.hotkey('ctrl', 'v')
 #para as cordenadas do mouse usamos mouseInfo() em outro terminal (F6 para salvar a coordenada)
    '''   
    descricao = coluna[1]
    categoria = coluna[2]
    codigo_pruduto = coluna[3]
    peso = coluna[4]
    dimensoes = coluna[5]
    preco = coluna[6]
    quantidade_em_estoque = coluna[7]
    data_de_validade = coluna[8]
    cor = coluna[9]
    tamanho = coluna[10]
    material = coluna[11]
    fabricante = coluna[12]
    pais_de_origem = coluna[13]
    observacoes = coluna[14]
    codigo_de_barras = coluna[15]
    localizacao_no_armazem = coluna[16]
'''
