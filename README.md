# AccuKnox_Assignment
## Topic 1: Django Signals

### Question 1: Are Django Signals Executed Synchronously or Asynchronously?

Answer:
By default, Django signals are executed synchronously.

### Explanation:
Signals run in the same process and block the caller until execution completes.
The handler's delay directly impacts the request or operation that triggered it.

### Proof from Code:
In the demo_signal_handler, we introduce a time.sleep(1) to simulate a delay.
The caller measures the time before and after the signal is triggered.
The minimal time gap between instance creation and signal execution confirms synchronous behavior.

### Question 2: Do Django Signals Run in the Same Thread as the Caller?

Answer:
Yes, Django signals run in the same thread as the caller by default.

### Explanation:
The caller thread and the signal thread are compared using threading.current_thread().
Since both threads are the same, it confirms that signals run in the same thread.
Implication:
If the signal handler contains blocking or time-consuming code, it will affect the caller's performance.

### Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?

Answer:
Yes, Django signals run in the same database transaction as the caller by default.
### Explanation:
When signals are triggered inside a transaction (transaction.atomic()), changes made within the signal are part of the same transaction.
If the transaction is rolled back, the signal changes will also be reverted.
This ensures data consistency.

### Proof from Code:
instance.refresh_from_db() verifies changes made by the signal within the same transaction.


## Topic 2: Custom Classes in Python

### Task: Create a Rectangle Class

Requirements:
A Rectangle class that takes length and width as integers.
The class should be iterable.
Iteration should yield a dictionary representing the length first, then the width.

### Explanation:
The __iter__() method is implemented using yield to create a generator.
This allows the Rectangle instance to be used in a for loop.
The first dictionary contains the length and the second contains the width.

### Expected Output:

{'length': 10}
{'width': 5}
This implementation ensures clarity and meets all given requirements efficiently.
