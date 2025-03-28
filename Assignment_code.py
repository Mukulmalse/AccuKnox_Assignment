# ----------------------
# Question 1: Synchronous Execution of Signals
# ----------------------
import threading
import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class DemoModel(models.Model):
    name = models.CharField(max_length=100)
    processed = models.BooleanField(default=False)

# Global variables to track signal behavior
signal_thread = None
signal_start_time = None
caller_thread = None

@receiver(post_save, sender=DemoModel)
def demo_signal_handler(sender, instance, created, **kwargs):
    global signal_thread, signal_start_time
    signal_thread = threading.current_thread()
    signal_start_time = time.time()

    # Simulate some processing
    time.sleep(1)
    instance.processed = True
    instance.save()

def create_model_instance():
    global caller_thread
    caller_thread = threading.current_thread()
    
    # Create model instance which triggers the signal
    instance = DemoModel.objects.create(name='Test')
    creation_time = time.time()

    print(f"Caller Thread: {caller_thread}")
    print(f"Signal Thread: {signal_thread}")
    print(f"Synchronous Execution: {abs(signal_start_time - creation_time) < 0.1}")

# ----------------------
# Question 2: Thread Execution
# ----------------------
# The previous code's output shows that caller_thread and signal_thread are the same.
# This proves that signals run in the same thread by default.

# ----------------------
# Question 3: Transaction Management
# ----------------------
from django.db import transaction

def demonstrate_transaction():
    with transaction.atomic():
        instance = DemoModel.objects.create(name='Transaction Test')
        print(f"Before Signal - Processed: {instance.processed}")

        # Signal modifies the instance
        instance.refresh_from_db()
        print(f"After Signal - Processed: {instance.processed}")




# ----------------------
# Topic: Custom Rectangle Class
# ----------------------
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

def demonstrate_rectangle():
    rect = Rectangle(10, 5)

    # Iteration
    for item in rect:
        print(item)

# Expected Output:
# {'length': 10}
# {'width': 5}
