import time

# def place_market_order(bot, symbol, side, qty):
#     try:
#         order = bot.client.futures_create_order(
#             symbol=symbol,
#             side=side,
#             type='MARKET',
#             quantity=qty
#         )
#         bot.logger.info(f"Market Order: {order}")
#         return order
#     except Exception as e:
#         bot.logger.error(f"Market Order Error: {str(e)}")
#         return None 

def place_market_order(bot, symbol, side, qty):
    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=qty
        )
        bot.logger.info(f"Market Order: {order}")
        print("[green]Market Order Placed Successfully[/green]")
        print(order)  # 👈 This will show full details in the terminal
        return order
    except Exception as e:
        bot.logger.error(f"Market Order Error: {str(e)}")
        print(f"[red]Market Order Error: {str(e)}[/red]")  # 👈 Also show error in terminal
        return None


def place_limit_order(bot, symbol, side, qty, price):
    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=qty,
            price=price
        )
        bot.logger.info(f"Limit Order: {order}")
        return order
    except Exception as e:
        bot.logger.error(f"Limit Order Error: {str(e)}")
        return None

def twap_order(bot, symbol, side, qty, intervals=5, delay=3):
    part_qty = round(qty / intervals, 3)
    orders = []
    for i in range(intervals):
        order = place_market_order(bot, symbol, side, part_qty)
        orders.append(order)
        time.sleep(delay)
    return orders
