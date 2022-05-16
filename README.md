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
run-local-servers.sh
wait
```

## Missing features
* Better logging support, probably using structlog
* Some kind of swagger UI client for the accounts service to use when calling the transactions service.  [This library looks like a good fit](https://github.com/commonism/aiopenapi3/) but it wasn't working when I tested it, I think it's being ported from an older library at the time of writing
* `pytest` package should have been installed as a dev dependency...

## CI/CD Notes
* Use Poetry in the build system to ensure that dependencies are pinned to whatever the developer makes them
* I usually try to have CI/CD "code" in local Makefiles, and have CI/CD run these make files, this helps avoid having parts of the build process stranded in some remote compute environment with developers pushing lots of silly `no change triggering build` commits
* Obvs the tests will run before any deployments
* Usually have config to run tests when merging a PR - if the tests fail then the PR is automatically rejected

## Testing Notes
* Prefer unit tests wherever possible because they're easier and faster to run and manage.  Integration tests can become problematic when there are lots of moving parts - intermittent test failures never inspire confidence...
* Use `unittest.mock` to mock out dependencies and target specific sections of code to test behaviors and outputs
* Mocking works best when you have properly decoupled code.  Having too many namespaces in the SUT is a code smell, and will mean you have a massive number of mocks :)
