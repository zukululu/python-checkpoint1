# Python Checkpoint 1

## There are 33 tests(assertions) total. 

#### You must get at least 60% to pass the checkpoint. This is equatable to passing at least 20 tests.

In the checkpoint directory you will find 3 files

data_types.py</br>
methods.py</br>
oop.py

Completing the Checkpoint & Running the Test
- There are instructions in side each of the files to guide you to passing the test.
- Additionally, if you attempt to run the test with `pytest`, it will give you an error message guiding you to what is needed to pass the test
- When running pytest it may not give you an accurate count of the tests, it counts only up to the tests that are complete
- Take the tests and instructions one step at a time
- Keeping the problems solve, your focus small, will make the problems easier to solve

#### Run the following commands to: clone the repo, enter the directory, create the environment, activate the environment, install the test dependencies in to the environment 
git clone </br>
cd </br>
python3 -m virtualenv .env</br>
source .env/bin/activate</br>
pip install -r requirements.txt</br>
pytest

## Exit and deactivate enviroment (You shouldn't need to run this!!!)
deactivate
rm -r .env
