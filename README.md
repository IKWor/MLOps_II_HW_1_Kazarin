# MLOps II. Домашнее задание №1 - Credit Default Analysis. Казарин Иван Владимирович.

## Описание
Этот проект включает настройку CI/CD пайплайна и проведение разведочного анализа данных (EDA) на основе датасета **Credit Default**. В ходе работы настроены этапы сборки, линтинга, тестирования и публикации Python-пакета, а также выполнен анализ данных, включающий визуализацию и расчёт корреляций между признаками.

## Наблюдения и выводы
Пропущенные значения: Датасет не содержит пропусков, что облегчает подготовку данных для анализа.

Дисбаланс классов: Большинство клиентов не допустили дефолт (около 85% данных), что может потребовать учета дисбаланса при обучении моделей.

Анализ признаков: Показатель отношения кредита к доходу (Loan to Income) оказывает значительное влияние на вероятность дефолта.

Корреляции: Слабая корреляция между возрастом и дефолтом, но сильная связь между отношением кредита к доходу и риском дефолта.

## Установка

Для локальной установки зависимостей выполните команду:
```bash
pip install -r requirements.txt
