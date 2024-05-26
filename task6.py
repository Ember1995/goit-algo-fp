class FoodItem:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    food_items = [FoodItem(name, data['cost'], data['calories']) for name, data in items.items()]
    food_items.sort(key=lambda x: x.ratio, reverse=True)

    total_calories = 0
    selected_items = []

    for item in food_items:
        if budget >= item.cost:
            budget -= item.cost
            total_calories += item.calories
            selected_items.append(item.name)

    return total_calories, selected_items

# Динамічне програмування
def dynamic_programming(items, budget):
    costs = [data['cost'] for data in items.values()]
    calories = [data['calories'] for data in items.values()]
    names = list(items.keys())
    n = len(costs)

    # Ініціалізуємо таблицю DP
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю DP знизу вгору
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif costs[i - 1] <= w:
                dp[i][w] = max(calories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Знаходимо вибрані страви
    total_calories = dp[n][budget]
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if total_calories <= 0:
            break
        if total_calories == dp[i - 1][w]:
            continue
        else:
            selected_items.append(names[i - 1])
            total_calories -= calories[i - 1]
            w -= costs[i - 1]

    return dp[n][budget], selected_items

if __name__ == "__main__":

    # Вхідні дані про їжу
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # Ліміт бюджету
    budget = 100

    # Результат жадібного алгоритму
    greedy_calories, greedy_items = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print(f"Загальна кількість калорій: {greedy_calories}")
    print(f"Вибрані страви: {greedy_items}")

    # Результат динамічного програмування
    dp_calories, dp_items = dynamic_programming(items, budget)
    print("\nДинамічне програмування:")
    print(f"Загальна кількість калорій: {dp_calories}")
    print(f"Вибрані страви: {dp_items}")
