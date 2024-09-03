import streamlit as st
import duckdb
import pandas as pd

# Função para carregar dados do arquivo Parquet
def load_data():
    con = duckdb.connect()
    df = con.execute("SELECT * FROM 'data/measurements_summary.parquet.py'").df()
    con.close()
    return df
   
# Convertendo o resultado para DataFrame
    df = result.df()  
    return df
# Função principal para criar o dashboard
def main():
    st.title("weather Station Summary")
    st.write("This dashboard shows the summary of weather staton")
    
    # Carregar os dados
    data = load_data()
    
    # Exibir os dados em formato de tabela
    st.dataframe(data)
    
if __name__ == "main__":
    main()