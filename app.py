from cost_analyzer import (
    calculate_total_cost, 
    get_highest_cost_serivce,
    calcualte_percentage,
    is_high_cost_percentage
)

print("AWS AI Cost Explainer")

aws_costs = {
    "EC2" : 420.50,
    "S3" : 85.20,
    "RDS" : 260.00,
    "Lambda" : 35.75,
}

print(aws_costs)
print("EC2 cost:", aws_costs["EC2"])
total_cost = calculate_total_cost(aws_costs)
print(f"Total AWS cost: ${total_cost:.2f}")

highest_cost_service = get_highest_cost_serivce(aws_costs)
print("Hightest cost service:", highest_cost_service)
highest_cost = aws_costs[highest_cost_service]
print(f"Highest cost: ${highest_cost:.2f}")

print("\nCost Breakdown:")

for service, cost in aws_costs.items():
    percentage = calcualte_percentage(cost, total_cost)
    print (f"{service}: ${cost:.2f} ({percentage:.1f}%)")

    if is_high_cost_percentage(percentage):
        print(f"Warning: {service} represents a large portion of your AWS bill.")


