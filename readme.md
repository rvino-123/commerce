# CS50WEB WEEK 3 PROJECT: COMMERCE


# Testing

## Testing the API
### Test Driven Development
- Write a test
- Run the test, ensure it fails. 
- Write some code to make the test pass. 
- Refactor when necessary. 
### Strategy
- Use PyTest in conjunction with the Factory approach to test the API. 
- Use Code Coverate as a measure of how much of the code is not covered by tests
### Dependencies
- `pytest` to run tests
- `pytest-django` to provide plugins to test Django applications
- `pytest-factoryboy` to facilitate using the factory approach to testing the Django app. 
- `Faker` to generate test data
- `pytest-cov` produces coverage reports
### Testing Setup
- All test files will be held in a single directory `tests`
  - Make sure to include an `__init__.py` to make it a package. 
- Create a directory per app i.e. `users` to test authentication. 
  - Make sure to include `__init__.py` for each one. 


### Configuring PyTest
- pytesting settings can be set in a config file, which by convention resides in root directory of the repo. 
- create `pytest.ini` which takes precedence over other files, even when empty
```
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = commerce.settings.development
python_files = tests.py tests_*.py *_tests.py

```
- In the tutorial I used, we put two config options in the pytest.ini
  - `DJANGO_SETTINGS_MODULE`: to point to the location of the settings file to be used (development) for the tests. 
  - `python_files`: determines which python files are considered test modules (seperate by space)

### Test Coverage
- in setup.cfg, add a section for `coverage:run` and `coverage:report`
  - add `source = .` to start at root directory
  - add `omit = ...` to tell coverage not to track those files.

### Factories
- Factories are python classes that behave like django classes
- We want to use LazyAttributes for attributes that are asigned when istance is generated and not a static value. 
  - Since we are using faker to generate fake values, we need to use LazyAttributes for those made up values.
- To ensure this is a clean test, so we should use `mute_signals(post_save)` to make sure there is no effect on our system.
