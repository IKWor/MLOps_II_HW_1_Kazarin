import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda():
    # Загрузка данных
    data = pd.read_csv('Credit_Default.csv')
    
    # Предварительный обзор данных
    print(data.head())
    
    # Анализ пропущенных значений
    missing_values = data.isnull().sum()
    print("Missing values:\n", missing_values)
    missing_values.plot(kind='bar')
    plt.show()
    
    # Диаграммы попарного распределения
    sns.pairplot(data, hue='Default')
    plt.show()
    
    # Корреляционный анализ
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.show()
    
    # Баланс классов
    class_balance = data['Default'].value_counts()
    print("Class balance:\n", class_balance)
    class_balance.plot(kind='bar')
    plt.show()
