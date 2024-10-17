import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(file_path):
    # Загрузка данных
    data = pd.read_csv(file_path)
    
    # 1. Предварительный обзор данных
    print("Предварительный обзор данных:")
    display(data.head())

    # 2. Анализ пропущенных значений
    print("\nАнализ пропущенных значений:")
    missing_values = data.isnull().sum()
    display(missing_values)

    # Визуализация пропущенных значений (bar chart)
    plt.figure(figsize=(8, 6))
    missing_values.plot(kind='bar')
    plt.title('Количество пропущенных значений в каждом столбце')
    plt.ylabel('Количество пропусков')
    plt.show()

    # Процентное соотношение пропущенных значений (pie chart)
    missing_percentage = (missing_values / len(data)) * 100
    missing_percentage = missing_percentage[missing_percentage > 0]  # Учитываем только столбцы с пропусками
    if not missing_percentage.empty:
        plt.figure(figsize=(8, 6))
        plt.pie(missing_percentage, labels=missing_percentage.index, autopct='%1.1f%%')
        plt.title('Процентное соотношение пропущенных значений')
        plt.show()

    # 3. Построение диаграмм попарного распределения признаков
    print("\nПостроение диаграмм попарного распределения признаков (Income, Age, Loan и Default):")
    sns.pairplot(data[['Income', 'Age', 'Loan', 'Default']], hue='Default')
    plt.show()

    # 4. Корреляционный анализ
    print("\nКорреляционный анализ:")
    corr_matrix = data[['Income', 'Age', 'Loan', 'Loan to Income']].corr()
    display(corr_matrix)

    # Визуализация корреляционной матрицы (heatmap)
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Корреляционная матрица признаков')
    plt.show()

    # 5. Анализ баланса классов
    print("\nАнализ баланса классов:")
    class_balance = data['Default'].value_counts()
    display(class_balance)

    # Визуализация распределения классов (bar chart)
    plt.figure(figsize=(8, 6))
    class_balance.plot(kind='bar', color=['skyblue', 'salmon'])
    plt.title('Распределение классов (Default)')
    plt.ylabel('Количество')
    plt.xticks(rotation=0)
    plt.show()
