#  AWS AI Cost Explainer

An AI-powered AWS cost analysis tool built with **Python, AWS Cost Explorer, Boto3, and Amazon Bedrock**.

The application retrieves AWS spending data, analyzes costs using Python, and uses Amazon Nova Lite through Bedrock to generate clear FinOps-style explanations and optimization recommendations.

## Features

- Retrieves real AWS billing data using Cost Explorer
- Supports real and demo data modes
- Calculates total spend and service-level percentages
- Identifies the highest-cost AWS service
- Flags major cost drivers
- Uses Amazon Bedrock to explain spending patterns
- Generates AWS cost optimization recommendations

## Architecture

```text
AWS Cost Explorer
       ↓
  aws_client.py
       ↓
cost_analyzer.py
       ↓
 ai_explainer.py
       ↓
Amazon Bedrock
  (Nova Lite)
       ↓
FinOps Insights
```

Python handles deterministic calculations, while Bedrock is used for explanation and contextual recommendations.

## Tech Stack

**Python • AWS Cost Explorer • Amazon Bedrock • Amazon Nova Lite • Boto3 • Git • GitHub**

## Structure

```text
├── app.py
├── aws_client.py
├── cost_analyzer.py
├── ai_explainer.py
├── requirements.txt
└── README.md
```

## Run Locally

```bash
git clone https://github.com/Sadeeee-n/aws-ai-cost-explainer.git
cd aws-ai-cost-explainer

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Choose:

- `real` — retrieves actual AWS Cost Explorer data
- `demo` — uses sample AWS spending data

Real mode requires configured AWS credentials and appropriate Cost Explorer and Bedrock permissions.

## AI Cost Analysis

The application sends analyzed cost information to **Amazon Nova Lite through Amazon Bedrock**.

The model generates:

- A spending summary
- Identification of the main cost driver
- FinOps-style optimization recommendations

Core calculations remain in Python rather than being delegated to the LLM.

## Why I Built This

I built this project to gain hands-on experience combining **AWS, Python, cloud cost management, and generative AI**.

It demonstrates how deterministic software logic can be combined with an LLM to turn cloud billing data into understandable and actionable insights.

## Development

Built using **VS Code, AWS CLI, Git, GitHub, and Claude Code** as an AI-assisted development tool.

## Future Improvements

- Web interface and dashboards
- Historical cost trends
- Interactive visualizations
- Configurable analysis periods
- Exportable FinOps reports

> AI-generated recommendations should be reviewed before making changes to production AWS infrastructure.
