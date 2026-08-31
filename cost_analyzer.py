def calculate_total_cost(costs):
    return sum(costs.values())

def get_highest_cost_serivce(costs):
    return max(costs, key = costs.get)

def calculate_percentage(cost, total_cost):
    return (cost / total_cost) * 100

def is_high_cost_percentage(percentage):
    return percentage > 40