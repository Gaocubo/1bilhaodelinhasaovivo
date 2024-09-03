import streamlit as st
import duckdb
import pandas as pd
import time

# Função para carregar dados do arquivo CSV e executar a xonsulta
def create_duckdb():
    result = duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station
    """)
# Convertendo o resultado para DataFrame
    df = result.df()  
    return df
# Função principal para criar o dashboard
def main():
    st.title("weather Station Summary")
    st.write("This dashboard shows the summary of weather staton")
    
    # Carregar os dados
    data = create_duckdb()
    
    # Exibir os dados em formato de tabela
    st.dataframe(data)
    
if __name__ == "main__":
    main()
    
    