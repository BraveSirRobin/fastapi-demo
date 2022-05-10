ACCOUNTS_SERVICE_PORT=8000
TRANSATIONS_SERVICE_PORT=8001

run-accounts-service:
	TRANSATIONS_SERVICE_PORT=${TRANSATIONS_SERVICE_PORT} uvicorn --port ${ACCOUNTS_SERVICE_PORT} accounts.app:app --reload

run-transactions-service:
	uvicorn --port ${TRANSATIONS_SERVICE_PORT} transactions.app:app --reload

clean:
	find . -name __pycache__ -type d -exec rm -rf {} \;