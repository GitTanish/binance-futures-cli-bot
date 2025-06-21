from bot import BasicBot
from orders import place_market_order, place_limit_order, twap_order
from rich.prompt import Prompt
from rich import print

def run():
    bot = BasicBot()
    print("[bold green]Binance Testnet Bot Connected[/bold green]")

    while True:
        print("\n[bold]Choose an order type:[/bold]\n1. Market\n2. Limit\n3. TWAP\n4. Exit")
        choice = Prompt.ask("Your choice", choices=["1", "2", "3", "4"])

        if choice == "4":
            print("[yellow]Goodbye![/yellow]")
            break

        symbol = Prompt.ask("Enter symbol", default="BTCUSDT")
        side = Prompt.ask("Buy or Sell?", choices=["BUY", "SELL"])
        qty = float(Prompt.ask("Quantity"))

        if choice == "1":
            place_market_order(bot, symbol, side, qty)
        elif choice == "2":
            price = Prompt.ask("Limit Price")
            place_limit_order(bot, symbol, side, qty, price)
        elif choice == "3":
            intervals = int(Prompt.ask("Number of intervals", default="5"))
            delay = int(Prompt.ask("Delay between orders (seconds)", default="3"))
            twap_order(bot, symbol, side, qty, intervals, delay)

if __name__ == "__main__":
    run()


