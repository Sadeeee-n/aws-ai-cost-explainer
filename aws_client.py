import boto3
from datetime import date, timedelta


def create_cost_explorer_client():
    return boto3.client("ce")


def get_recent_costs():
    client = create_cost_explorer_client()

    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.isoformat(),
            "End": end_date.isoformat()
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    costs = {}

    for results in response ["ResultsByTime"]:
        for group in results["Groups"]:
            service_name = group["Keys"][0]
            amount = float(group["Metrics"]["UnblendedCost"]["Amount"])


            if service_name in costs:
                costs[service_name] += amount
            else:
                costs[service_name] = amount

    return costs