# test-argparse

Tiny example on how to test an argparse.

Inspired by:

* [How do you write tests for the argparse portion of a python module?](https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module)

## Example

```python
def test_main_flow(self):
    # equivalent to: python src/api.py --name "Jane Doe"
    env = {"foo": "bar"}
    args = ["main.py", "--name", "Jane Doe"]
    run_main(self.abs_path, args, env) 
```

## Usage

Run with

```
python src\api.py --name "Jane Doe"
```

Run the test with 

```bash
pytest
```