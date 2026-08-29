import boto3


def create_bedrock_client():
    return boto3.client("bedrock-runtime", region_name="us-east-1")


def explain_costs(costs, total_cost, highest_cost_service):
    client = create_bedrock_client()

    prompt = f"""
You are an AWS FinOps cost analyst.

Analyze the following AWS spending data:

{costs}

Total monthly cost: ${total_cost:.2f}
Highest cost service: {highest_cost_service}

Your job is to:

1. Summarize the overall AWS spending pattern.
2. Identify the biggest cost driver.
3. Explain why that service may be expensive.
4. Give exactly 3 practical AWS cost optimization recommendations.
5. Prioritize recommendations that are specific to the services shown in the data.
6. Do not invent usage metrics, utilization percentages, or savings amounts that were not provided.

Use clear language suitable for a junior cloud engineer.

Format the response using these headings:

Spending Summary
Main Cost Driver
Optimization Recommendations
"""

    response = client.converse(
        modelId="amazon.nova-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return response["output"]["message"]["content"][0]["text"]