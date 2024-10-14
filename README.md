# Bot de marcas

O bot faz a leitura de uma planilha em Excel e insere as marcas dentro do Intelliauto de forma prática e rápida,
além de contar com opções de execução. 


# Estrutura do Excel 

A planilha deve seguir esse exemplo: 
|                |Marcas|                        
|----------------|-------------------------------|
|1|`X`            |
|2|`Y`            |
|3|`Z`|

## Estrutura do projeto 
Deve ser criado uma pasta **Folder** dentro do escopo do projeto, onde irá guardar o Excel. e também deve ser alterado o caminho na linha **7** df = pd.read_excel(**'../file/seuExcel.xlsx'**)

## Capturar coordenadas do cursor

Rode o arquivo **captureCursor.py** e capture onde aparece a região do select para o bot poder clicar, o ambiente deve ser fixo. e troque as linhas 

Select:
**28: pyautogui.click(x=-1361, y=448)**

Clique na opção:
**55: pyautogui.click(x=-1330, y=567)**
