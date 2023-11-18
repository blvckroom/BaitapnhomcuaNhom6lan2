k = [4.95, 9.95, 14.95, 19.95, 24.95]
new_prices = []
print('old price \t discount \t new price \n')
for i in range(0, len(k)):
    new_prices.append(60 * k[i] / 100)
    print(f"{k[i]:5.2f} \t {round(k[i] - new_prices[i], 2):5.2f}  \t {new_prices[i]:5.2f}")