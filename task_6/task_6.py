def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = {}
    total_cost = 0
    total_calories = 0
    
    for item, values in sorted_items:
        if total_cost + values['cost'] <= budget:
            selected_items[item] = values
            total_cost += values['cost']
            total_calories += values['calories']
    
    return selected_items, total_cost, total_calories






def dynamic_programming(items, budget):
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    selected_items = {}
    
    for i, (item, values) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if values['cost'] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - values['cost']] + values['calories'])
    
    j = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items[list(items.keys())[i - 1]] = items[list(items.keys())[i - 1]]
            j -= items[list(items.keys())[i - 1]]['cost']
    
    total_cost = sum(selected_items[item]['cost'] for item in selected_items)
    total_calories = sum(selected_items[item]['calories'] for item in selected_items)
    
    return selected_items, total_cost, total_calories




items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
print("\nGreedy Algorithm:")
print(f"Selected Items: {', '.join(item for item in selected_items)}")
print("Total Cost:", total_cost)
print("Total Calories:", total_calories)

# Динамічне програмування
selected_items, total_cost, total_calories = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print(f"Selected Items: {', '.join(item for item in selected_items)}") 
print("Total Cost:", total_cost)
print("Total Calories:", total_calories)