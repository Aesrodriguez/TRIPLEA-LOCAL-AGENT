from tools.filesystem import FileSystemTool

print("=" * 50)
print("PRUEBA FILESYSTEM")
print("=" * 50)

print(FileSystemTool.list_directory("."))

FileSystemTool.create_directory("temp")

FileSystemTool.create_file("temp/hola.txt")

FileSystemTool.write_file(
    "temp/hola.txt",
    "Hola TripleA"
)

print(FileSystemTool.read_file("temp/hola.txt"))

print(FileSystemTool.exists("temp/hola.txt"))

print(FileSystemTool.find_files(".", "*.py"))