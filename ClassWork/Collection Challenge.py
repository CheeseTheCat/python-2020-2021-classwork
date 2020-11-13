#James Hooper
#6.2 Collection Challenge

collection = [3.14159, "Ahoy", True, 42, -1000, "Mmmmmm, ice cream"]
print("starting collection: {}",collection)

collection.reverse()
collection.remove("Mmmmmm, ice cream")
collection.insert(0,"Cookies")
collection.remove(-1000)
collection.insert(1,"Second")
collection.remove(42)
collection.insert(2,43)

print("Transformed collection: {}",collection)
#['Cookies', 'Second', 43, True, 'Ahoy', 3.14159]
