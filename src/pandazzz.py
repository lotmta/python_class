import pandas as pd


produccion = pd.Series([5, 11, 4, 7, 2],
                        index= ['gen1', 'gen2', 'gen3', 'gen4', 'gen5'])

costos = pd.Series([ 5, 4.3, 7, 3.5],
                  index=['gen5', 'gen2', 'gen3', 'gen1'])

num_genes = pd.read_csv('data/num_genes.csv',index_col='Organism').squeeze()

top_5_genoma_big = num_genes.sort_values(ascending=False).head()

print(top_5_genoma_big.plot.bar())
