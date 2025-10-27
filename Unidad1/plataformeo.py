from platform import version,platform, machine, system, python_implementation, python_version_tuple
print(python_implementation())

for atr in python_version_tuple():
    print(atr, end='')
print()

print(version())
print(system(), end='')
print(machine())

print(platform())
print(platform(1))
print(platform(0, 1))