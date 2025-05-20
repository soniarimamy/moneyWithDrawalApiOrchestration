# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Metadata
LABEL name="money_withdraw_api_orchestration_prod"

# Create application directory
WORKDIR /home/money_withdraw_api_orchestration_prod

# Copy only requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies first (leveraging cache if requirements.txt hasn't changed)
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Now copy the rest of the application code
COPY . .

# Set the default command to run your application
CMD ["python", "moneyWithdrawalApiOrchestration-core.py"]