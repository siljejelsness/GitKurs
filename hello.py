import pathlib

path = pathlib.Path("hello.md")

print("OVERSKRIFT")
print(path.read_text())

# doing something