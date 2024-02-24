import random

class Tools:
    def __init__(self) -> None:
        pass
def generate_random_id():
    # Generate random id start with regex SE{000000}
    random_id = "SE" + ''.join(random.choices('0123456789', k=6))
    return random_id