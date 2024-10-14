# 0x01-python_async_function

## Description
This project demonstrates the usage of asynchronous programming in Python using the `async` and `await` syntax. The project includes various examples of running asynchronous tasks concurrently, measuring execution time, and creating tasks using `asyncio`.

## Learning Objectives
By the end of this project, you will be able to:
- Understand the `async` and `await` syntax in Python.
- Execute asynchronous programs using `asyncio`.
- Run concurrent coroutines.
- Create and manage `asyncio` tasks.
- Use the `random` module to introduce delays in coroutines.

## Project Structure
- **0-basic_async_syntax.py**: Contains the `wait_random` coroutine that waits for a random delay and returns it.
- **1-concurrent_coroutines.py**: Defines the `wait_n` coroutine, which spawns `wait_random` n times and returns the delays in ascending order.
- **2-measure_runtime.py**: Implements the `measure_time` function to calculate the average runtime of `wait_n`.
- **3-tasks.py**: Defines the `task_wait_random` function, which returns an `asyncio.Task` for the `wait_random` coroutine.
- **4-tasks.py**: Contains the `task_wait_n` coroutine, which uses `task_wait_random` to manage tasks concurrently.

## Requirements
- Python 3.7+
- Ubuntu 18.04 LTS
- Adherence to PEP 8 style guide
- All functions and coroutines are type-annotated and documented
- Files must be executable and tested using `wc` for length

## How to Run
1. Clone the repository and navigate to the project directory.
2. Run the main test files to see outputs:
   ```bash
   python3 0-main.py
   python3 1-main.py
   python3 2-main.py
   python3 3-main.py
   python3 4-main.py
