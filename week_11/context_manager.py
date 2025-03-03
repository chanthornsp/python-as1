from contextlib import contextmanager

class CustomContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"Error occurred: {exc_value}")
        return False  # ensure the exception is propagated
    
# with CustomContextManager() as c:
#     print('Inside the context')
#     raise ValueError("Something went wrong")



@contextmanager
def custom_context_manager():
    print("Entering the context")
    yield "Resource"
    print("Exiting the context")

# Usage
with custom_context_manager() as resource:
    print("Inside the context")
    # print("Resource:", resource)