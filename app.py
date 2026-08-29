from aws_client import create_cost_explorer_client, get_recent_costs

from ai_explainer import create_bedrock_client

from ai_explainer import explain_costs

from cost_analyzer import (
    calculate_total_cost, 
    get_highest_cost_serivce,
    calcualte_percentage,
    is_high_cost_percentage
)

from ai_explainer import create_bedrock_client


print("AWS AI Cost Explainer")

demo_costs = {
    "Amazon EC2": 420.50,
    "Amazon S3" : 85.20,
    "Amazon RDS" : 260.00,
    "AWS Lambda" : 35.75,
}

mode = input("Choose mode: real or demo: ").strip().lower()


if mode == "real":
    try:
        aws_costs = get_recent_costs()
        print("Using real AWS Cost Explorer data.")

    except NoCredentialsError:
        print("AWS credentials not found. Please configure your AWS credentials.")
        exit()
    except ClientError as error:
        print(f"An error occurred while fetching AWS costs: {error}")
        print("error")

        use_demo = input("Would you like to use demo data instead? (yes/no):").strip().lower()
        if use_demo == "yes":
            aws_costs = demo_costs
            print("Using demo AWS cost data.")
        else:
            exit()

elif mode == "demo":
    aws_costs = demo_costs
    print("Using demo AWS cost data.")

else:
    print("Invalid mode selected. Please choose 'real' or 'demo'.")
    exit()

    print("\nAI Cost Explanation:")

    ai_explanation = explain_costs(
        aws_costs,
        total_cost,
        highest_cost_service
    )

    print(ai_explanation)

total_cost = calculate_total_cost(aws_costs)
print(f"Total AWS cost: ${total_cost:.2f}")

highest_cost_service = get_highest_cost_serivce(aws_costs)
print("Highest cost service:", highest_cost_service)
highest_cost = aws_costs[highest_cost_service]
print(f"Highest cost: ${highest_cost:.2f}")

print("\nCost Breakdown:")

for service, cost in aws_costs.items():
    percentage = calcualte_percentage(cost, total_cost)
    print (f"{service}: ${cost:.2f} ({percentage:.1f}%)")

    if is_high_cost_percentage(percentage):
        print(f"Warning: {service} represents a large portion of your AWS bill.")

print("\nAI Cost Analysis:")

ai_response = explain_costs(
    aws_costs,
    total_cost,
    highest_cost_service
)

print(ai_response)

