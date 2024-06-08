import pandas as pd
import streamlit as st

from models.instance import SKLEARN_MODEL, X_TRAIN_COLUMNS

file = st.file_uploader(label="Seu arquivo de escoragem", type=["ftr", "csv", "xlsx"])

extensions = {"ftr": pd.read_feather, "xlsx": pd.read_excel, "csv": pd.read_csv}

if file is not None:
    file_extension = file.name.split(".")[-1]
    if file_extension in extensions:
        df: pd.DataFrame = extensions[file_extension](file).drop(
            columns=["index", "data_ref", "mau"]
        )
    else:
        st.error(
            "Extensão de arquivo não suportada. Por favor, carregue um arquivo com extensão .ftr, .csv ou .xlsx."
        )

    X = pd.get_dummies(df)
    for col in X_TRAIN_COLUMNS:
        if col not in X.columns:
            X[col] = 0

    pred = SKLEARN_MODEL.predict(X)
    df["Recebeu Crédito?"] = df["Recebeu Crédito?"] = pd.Series(pred).map(
        {1: "Sim", 0: "Não"}
    )
    st.dataframe(df, hide_index=True)
