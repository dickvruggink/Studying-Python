# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

#Part 1


from decimal import ROUND_UP


leek_price = str(2)
print('Leek is ' + leek_price + ' euro per kilo.')

#Part 2

order = 'Leek 4'
order_amount = int(order[order.find(' '):])
leek_sum_total = (order_amount * int(leek_price))
print(leek_sum_total)

#Part 3

broccoli_kilo_price = 2.34
order_amount_broccoli = 1.6
total_price_broccoli = (broccoli_kilo_price * order_amount_broccoli)
print('1.6kg broccoli costs ' + str(round(total_price_broccoli, 2)) + 'e')
