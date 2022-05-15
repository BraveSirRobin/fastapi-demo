# Enterprise Python - FastAPI

This repo is a demo of some of the enterprise features available in the Python FastAPI project.  We demo a couple of different API servers which interact to emulate a simple bank account and transaction service.

## Setting up your enviroment
You'll need to install Poetry, then run:
```
poetry install
poetry shell
```

## Some nice features

* All request/response models are defined as Pydantic models.  This allows the programmer to define the input / output of microservices in a declarative style, and gives you a level of "type safety" without having to write lots of boilerplate validation code
* Each service comes with a [built-in API documentation page](http://127.0.0.1:8000/docs#) which allows you to make test calls to your service.
* Service configuration is also managed by Pydantic, you can provide this using a env file (prob for development) or using environment variable, a-la 12-factor apps in your cloud environments.
* Bundled tests show how to execute your API endpoints with simple Python calls, allowing you to run full tests on API endpoints with support for mocking

## How to run
For local development you'll need to enter the Poetry shell then run both services, e.g. using the Makefile
```
poetry shell
make run-accounts-service && make run-transactions-service
wait
```

## Missing features
* Better logging support, probably using structlog
* Some kind of swagger UI client for the accounts service to use when calling the transactions service