class Student:
    group = "C2011"
    education = "STEP"

    def __init__(self, name, age):
        self.name = name
        self.age = age


st1 = Student(name="Roman", age=13)
st2 = Student(name="Igor", age=12)

print(f"Info st1 = {st1.name}, {st1.age}, {st1.group}")
print(f"Info st2 = {st2.name}, {st2.age}, {st2.group}")