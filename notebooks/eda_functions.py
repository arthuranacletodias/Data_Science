# use essa função sempre que vc quiser ver todas as linhas e colunas de um dataframe

def show_all(df):
    
    # setando opções sem limites
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', None)
    
    display(df)
    
    # resetando opções pro padrão    
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('max_colwidth')

#


