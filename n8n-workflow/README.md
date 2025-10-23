# n8n Invoice Workflow

This n8n workflow is an agentic AI-powered invoice generator that automates validation, HTML template creation, PDF conversion, and email sending. It uses multi-agent collaboration with Google Gemini, Tavily search, and structured output parsing for efficient billing automation.

## Overview
The workflow processes invoice data from a sheet, validates entries using AI, generates HTML templates, converts them to PDF, and sends via email if provided. It's designed for freelancers and small businesses to save time on manual invoicing.

## Prerequisites
- n8n installed (self-hosted or cloud).
- API keys for:
  - Google Gemini (for AI processing).
  - Tavily (for search).
- Access to a Google Sheet or similar data source.

## Setup
1. Import the workflow JSON file (`invoice_workflow.json`) into your n8n instance via the workflow editor.
2. Configure nodes:
   - "Get rows in sheet": Connect to your data source (e.g., Google Sheet).
   - "Google Gemini Model": Add your API key.
   - "Search in Tavily": Add Tavily API key.
   - "Send a message": Configure email credentials (e.g., Gmail SMTP).
3. Test the workflow by executing it step by step.

## Workflow Description
The workflow structure is as follows:
- **When clicking Execute workflow**: Triggers the process.
- **Get rows in sheet**: Fetches invoice data from the source.
- **Loop Over Items**: Iterates over each item/entry.
- **Code in JavaScript**: Custom logic for data preparation.
- **Google Gemini Model**: AI agent for validation and processing.
- **Search in Tavily**: Searches for additional data if needed.
- **Structured Output Parser**: Parses AI output into structured format.
- **Generate HTML Template**: Creates dynamic HTML invoice.
- **Convert HTML to PDF**: Converts HTML to PDF file.
- **Check Email Provided**: Checks if email is available.
- **Send a message**: Sends the PDF via email or notifies.

This multi-agent setup ensures accuracy and efficiency in invoice generation.

## Workflow Technical Details
- **Tavily Search Tool**: Used to fetch current sales tax rate for the country. Query: "current {{ $json.results[0].current_date }} sales tax or VAT rate in {{ $json.results[0].country }}". Returns numeric rate as decimal (e.g., 0.18 for 18%).
- **AI Agent System Message**: You are a helpful assistant and an Invoice Processing Agent. Tasks: Validate & Clean Data, Calculate Subtotal, Fetch Tax Rate, Calculate Totals.
- **User Message**: This is the client data. {{ $json.results.map(item => JSON.stringify(item,null,2)).join("\n\n")}}
- **Structured Output Parser Schema**:  
```
{
    "type": "object",
    "additionalProperties": false,
    "properties": {
        "client_name": { "type": "string" },
        "address": { "type": "string" },
        "email": { "type": "string" },
        "country": { "type": "string" },
        "description": { "type": "string" },
        "rate_per_hour": { "type": "number" },
        "hours": { "type": "number" },
        "current_date": { "type": "string"},
        "invoice_number": { "type": "string" },
        "subtotal": { "type": "number", "description": "total before tax" },
        "tax": {
            "type": "object",
            "properties": {
                "rate": { "type": "number" },
                "amount": { "type": "number" }
            },
            "required": ["rate", "amount"]
        },
        "grand_total": { "type": "number", "description": "final total after tax" }
    },
    "required":["client_name"]
}
```


## Usage
1. Run the workflow with your data sheet.
2. Monitor the execution for any errors.
3. The output is a PDF invoice sent via email or logged.

## Contributions
Pull requests are welcome! If you have improvements or bug fixes, fork the repo and submit a PR.

## License
MIT License

## Contact
Shahzain Ali - [LinkedIn](https://www.linkedin.com/in/shahzain-ali-518b862ba/)
