# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:38:57 2023

@author: Richard
"""

import pandas as pd

path = "C:/Users/richa/Downloads/"
arq = "diabetes.csv"

dtypesDict = {"Pregnancies":int,
              "Glucose":int,
              "BloodPressure":int,
              "SkinThickness":int,
              "Insulin":int,
              "BMI":str,
              "DiabetesPedigreeFunction":str,
              "Age":int,
              "Outcome":int}

# LENDO O ARQUIVO #
df_diabetes = pd.read_csv(path+arq, 
                          encoding='UTF-8', 
                          engine='python', 
                          sep=',',
                          dtype=dtypesDict)

# REALIZANDO ALTERAÇÕES NECESSÁRIAS
df_diabetes["DiabetesPedigreeFunction"] = df_diabetes["DiabetesPedigreeFunction"].str.replace('.',',')
df_diabetes["BMI"] = df_diabetes["BMI"].str.replace('.',',')

# RETIRANDO PRESSÃO SANGUÍNEA IGUAL A 0 POR SER UM POSSÍVEL ERRO
valor = [0]
df_diabetes = df_diabetes.drop(df_diabetes[df_diabetes["BloodPressure"].isin(valor)].index)

# ARRUMANDO A ORDEM DOS VALORES
df_diabetes = df_diabetes.sort_values(by=["Age"])

# SALVANDO O ARQUIVO COMO UM EXCEL

with pd.ExcelWriter(f"{path}Diabetes_final.xlsx") as writer:
    df_diabetes = df_diabetes.sort_values(by=["Age"])
    df_diabetes.to_excel(writer, sheet_name = "Diabetes", index=False)