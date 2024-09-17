# 1) Question - Django Signal Demo

This project demonstrates the synchronous execution of Django signals. By default, Django signals are executed in a blocking manner, meaning that the signal handler (receiver) will be called immediately and must complete before further code execution continues.

## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Shirodkar-Shubham-GitHub/Django_Assignment.git
    cd your_repository
    ```

2. Run the migrations:
    ```sh
    python manage.py migrate
    ```

3. Start the development server:
    ```sh
    python manage.py runserver
    ```

4. Navigate to the following URL to trigger the signal:
   ```sh
    http://127.0.0.1:8000/create-user/
    ```

## Sample Signal Synchrony Output
   ```sh
    Before signal: 2024-09-15 12:43:40.446308
    Signal received for User: testuser3
    Signal processing completed for User: testuser3
    After signal: 2024-09-15 12:43:45.790104
    ```

# 2) Question - Django Signals Same Thread Demonstration

This project demonstrates that Django signals run in the same thread as the caller by default. When a signal is triggered, its handler executes in the same thread that triggered it, blocking the execution of the caller until the signal handler finishes running.


## Follow the 4 steps of Installation and Setup.

4. Navigate to the following URL to trigger the signal:
   ```sh
    http://127.0.0.1:8000/create/
    ```

## Sample Signal Thread Output
   ```sh
    Caller thread: Thread-1 (process_request_thread)
    Signal handler thread: Thread-1 (process_request_thread)
    ```


# 3) Question - Django Signal Transaction Demonstration

This Django project demonstrates that Django signals (like post_save) run in the same database transaction as the caller by default. If the transaction is rolled back, the signal handler's actions are also rolled back.


## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Shirodkar-Shubham-GitHub/Django_Assignment.git
    cd your_repository
    ```

2. Create and activate a virtual environment (optional):
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install Django:
    ```sh
    pip install django
    ```

4. Set up the Django project:
   ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the signal test: Use the custom management command to test signal and transaction behavior:
   ```sh
    python manage.py test_signal
    ```

## Sample Signal Transaction Output
   ```sh
    Creating a MyModel instance
    Signal received! Instance ID: 1
    Raising exception to trigger rollback
    Transaction rolled back due to: Simulating an error
    Check if the object exists: False
    ```

