import heapq

grades = [45, 643, 656, 33, 63, 76, 939, 5]

print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'FB', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'TUNA', 'price': 68}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))
