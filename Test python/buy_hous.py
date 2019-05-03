price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price - (0.1 * price)
else:
    down_payment = price - (0.2 *price)

print(down_payment)