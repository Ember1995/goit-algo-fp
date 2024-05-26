import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def cubes_toss(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # Ініціалізація лічильників для сум від 2 до 12

    for _ in range(num_rolls):
        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)
        cubes_sum = cube1 + cube2
        sums_count[cubes_sum] += 1

    return sums_count

# Функція для обчислення імовірностей
def calculate_probabilities(sums_count, num_rolls):
    probabilities = {}  # Створюємо порожній словник для зберігання ймовірностей
    for sum_value, frequency in sums_count.items():
        # Обчислюємо ймовірність як частку частоти (frequency) від загальної кількості кидків (num_rolls), помножену на 100 для отримання відсотків
        probabilities[sum_value] = (frequency / num_rolls) * 100
    return probabilities  # Повертаємо словник з ймовірностями

# Функція для виведення результатів у вигляді таблиці
def print_results(probabilities, analytical_probabilities):
    results = []
    results.append("Сума | Практичні результати (%) | Аналітичний розв'язок (%)")
    results.append("-----|--------------------------|--------------------------")
    for sum_value in sorted(probabilities.keys()):
        practical = probabilities[sum_value]
        analytical = analytical_probabilities.get(sum_value, 0)
        results.append(f"{sum_value:>4} | {practical:>24.2f} | {analytical:>23.2f}")
    
    return "\n".join(results)

# Функція для побудови графіку
def plot_probabilities(probabilities, filename='probabilities.png'):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='#1296F0', alpha=0.7)
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xticks(sums)
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    # Кількість симуляцій
    num_rolls = 1000000  # 1 мільйон кидків

    # Симуляція кидків
    sums_count = cubes_toss(num_rolls)

    # Обчислення імовірностей
    probabilities = calculate_probabilities(sums_count, num_rolls)

    # Аналітичні імовірності для порівняння
    analytical_probabilities = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

    # Виведення результатів у вигляді таблиці
    results_table = print_results(probabilities, analytical_probabilities)
    print(results_table)

    # Побудова графіку
    plot_probabilities(probabilities)

    # Запис результатів у файл README
    with open("README.md", "w") as f:
        f.write("# Task 7: Використання методу Монте-Карло\n\n")
        f.write("## Результати експерименту\n\n")
        f.write("![Ймовірності сум при киданні двох кубиків](probabilities.png)\n\n")
        f.write("```\n")
        f.write(results_table)
        f.write("\n```\n\n")
        f.write("## Висновки\n\n")
        f.write("Практичні результати методу Монте-Карло дуже близькі до аналітичних розрахунків, що підтверджує високу точність цього методу для обчислення ймовірностей. Крім того, сума всіх ймовірностей для можливих результатів також дорівнює 1 (або 100%), що демонструє правильність і повноту проведених обчислень. Це свідчить про ефективність методу Монте-Карло для моделювання випадкових процесів, таких як кидання кубиків.\n")
