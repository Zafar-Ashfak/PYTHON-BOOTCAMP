# No. This set itself is invalid in Python.

# s = {8, 7, 12.5, "Harry", [12, 7]} # Cannot use unhashable type 'list' as a set element

# You'll get:

# TypeError: unhashable type: 'list'
# Why?

# A set can only contain hashable (immutable) objects.

# ✅ Allowed:

s = {8, 7, 12.5, "Harry", (12, 7)}

# because tuples are immutable.

# ❌ Not allowed:

# s = {8, 7, 12.5, "Harry", [12, 7]}

# because lists are mutable.

# So can we change the values inside the list?

# No, because the set cannot even be created with a list inside it.