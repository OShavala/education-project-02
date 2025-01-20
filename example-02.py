days = int(input("Введіть кількість днів: "))
hours = int(input("Введіть кількість годин: "))
minutes = int(input("Введіть кількість хвилин: "))

total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60)
print("Загальна кількість секунд:", total_seconds)