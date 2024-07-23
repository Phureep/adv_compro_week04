children = [ {"name": "Alice", "age": 2, "height": 95}, 
            {"name": "Bob", "age": 4, "height": 105}, 
            {"name": "Charlie", "age": 3, "height": 110}, 
            {"name": "David", "age": 5, "height": 102}, 
            {"name": "Eve", "age": 6, "height": 99} ]

eligible_children = list(filter(lambda c: True if c["age"] > 3 and c["height"] > 100 else False , children))

print(eligible_children)

