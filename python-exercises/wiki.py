import wikipedia

phrase = input("Search Wikipedia: ")

results = wikipedia.search(phrase)

print("\nSearch results:")
for result in results:
    print("-", result)