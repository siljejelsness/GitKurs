import pathlib

print("Hello Git")
path = pathlib.Path("hello.md")
print(path.read_text())

# doing something