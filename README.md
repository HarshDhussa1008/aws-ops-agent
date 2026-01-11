# AWS Ops Agent

This project contains a Python-based AWS Operations Agent. The agent is designed to perform various operations and tasks related to AWS services.

## Project Structure

```
aws-ops-agent/
├── app.py               # Main entry point for the application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not tracked by Git)
├── .env.example         # Example environment variables file
├── .gitignore           # Git ignore rules
├── agent/               # Core agent logic
│   ├── agent.py         # Agent implementation
│   ├── tools.py         # Utility tools for the agent
│   └── __pycache__/     # Compiled Python files (ignored by Git)
└── __pycache__/         # Compiled Python files (ignored by Git)
```

## Prerequisites

- Python 3.8 or higher
- AWS CLI configured with appropriate credentials

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd aws-ops-agent
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   - Copy `.env.example` to `.env` and update the values as needed.

## Usage

Run the application using the following command:
```bash
python app.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.