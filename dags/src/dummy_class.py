import random

from klym_telemetry.utils import instrument, klym_telemetry

@instrument(private_methods=True)
class VectorClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scalar_mul(self, scalar):
        return (self.x * scalar, self.y * scalar)

    def sum(self, vector):
        return VectorClass(self.x + vector.x, self.y + vector.y)


@instrument(private_methods=True)
class DummyClass:

    def __init__(self):
        self.step_1()
        self.step_2()
        self.step_3()
        self.add_counter()

    def step_1(self):
        klym_telemetry.add_event_curr_span("Start vector scalar multiplication")
        vector = VectorClass(x=random.randint(1,10), y=random.randint(1,10))
        vector_scalar_mul = vector.scalar_mul(scalar=random.randint(1,10))
        klym_telemetry.add_event_curr_span("Vector scalar multiplication ready!")
        klym_telemetry.set_attr_curr_span("vector_mul", vector_scalar_mul)

    def step_2(self):
        klym_telemetry.add_event_curr_span("Start vector sum")
        vector_1 = VectorClass(x=random.randint(1,10), y=random.randint(1,10))
        vector_2 = VectorClass(x=random.randint(1,10), y=random.randint(1,10))
        vector_1.sum(vector_2)
        klym_telemetry.add_event_curr_span("Vector sum ready!")

    def step_3(self):
        print("step 3")

    @staticmethod
    def add_counter():
        klym_telemetry.up(name='dummy_class_klym_telemetry', description='Adding Counter to Klym Telemetry')
        print('klym telemetry up')
