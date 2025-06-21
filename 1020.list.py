fruits = ['apple', 'banana', 'cherry']
print(fruits)

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

colors = ['red', 'green']
colors.extend(['pink', 'purple'])
print(colors)

animals = ['fish', 'rat', 'cat']
animals.insert(1, 'hamster')
print(animals)

cities = ['London', 'Paris', 'New York', 'Sydney']
cities.remove('Paris')
print(cities)

languages = ['Python', 'Java', 'C++']
removed = languages.pop(0)
print(languages, removed)

scores = [88, 76, 92, 43]
scores.sort()
print(scores)

letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)

nums = [1, 0, 3, 2, 1, 1, 3,2, 4]
count_2 = nums.count(2)
print(count_2)

original = [5, 10, 15]
copy_list = original.copy()
print(copy_list)