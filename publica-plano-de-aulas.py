import tabulate
import pandas as pd

t1 = pd.read_excel('plano-de-aulas.xlsx')
#t1['Data'] = t1['Data'].apply(lambda x: x.strftime('%d/%m'))

with open('docs/_snippets/plano-de-aulas.md', 'w') as f:
    tabela_str = tabulate.tabulate(t1[['Data', 'Questão/Problema/Desafio',
'Conteúdo']], headers=['Data', 'Questão/Problema/Desafio',
'Conteúdo'], tablefmt='pipe', showindex=False)
    f.write(tabela_str)
