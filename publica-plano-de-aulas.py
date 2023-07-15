import tabulate
import pandas as pd

t1 = pd.read_excel('plano-de-aulas.xlsx')
t1['Date'] = t1['Date'].apply(lambda x: x.strftime('%d/%m'))

with open('docs/_snippets/plano-de-aulas.md', 'w') as f:
    tabela_str = tabulate.tabulate(t1[['Date', 'Question/Problem/Challenge',
'Content']], headers=['Date', 'Question/Problem/Challenge',
'Content'], tablefmt='pipe', showindex=False)
    f.write(tabela_str)
