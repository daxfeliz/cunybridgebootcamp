msg = 'Hello '
print(msg)

# Example greeting
name = None   # BUG: should be a string, but it's None
name = 'World'

# This will raise an AttributeError
greeting = msg + name.strip() + "!"
print(greeting)


