ACCOUNTS_SERVICE_PORT=8000
TRANSATIONS_SERVICE_PORT=8001

run-accounts-service:
	uvicorn --port ${ACCOUNTS_SERVICE_PORT} accounts.main:app --reload

run-transactions-service:
	uvicorn --port ${TRANSATIONS_SERVICE_PORT} transactions.main:app --reload

clean:
	find . -name __pycache__ -type d -exec rm -rf {} \;