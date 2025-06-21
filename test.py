#!/usr/bin/env python3
"""
Test script to verify Binance Testnet connection
"""

from bot import BasicBot
from rich import print
from rich.console import Console
from rich.table import Table

def test_connection():
    """Test basic connection to Binance Testnet"""
    console = Console()
    
    print("[bold blue]🚀 Testing Binance Futures CLI Bot Connection...[/bold blue]\n")
    
    try:
        # Initialize bot
        print("[yellow]⏳ Initializing bot...[/yellow]")
        bot = BasicBot()
        print("[green]✅ Bot initialized successfully![/green]")
        
        # Test server time
        print("[yellow]⏳ Testing server connection...[/yellow]")
        server_time = bot.client.get_server_time()
        print(f"[green]✅ Server time: {server_time}[/green]")
        
        # Test account info
        print("[yellow]⏳ Testing account access...[/yellow]")
        account_info = bot.client.futures_account()
        print("[green]✅ Account access successful![/green]")
        
        # Display balance
        print("[yellow]⏳ Fetching account balance...[/yellow]")
        balance = bot.get_balance()
        
        if balance:
            print("[green]✅ Balance retrieved successfully![/green]\n")
            
            # Create a nice table for balance display
            table = Table(title="💰 Account Balance")
            table.add_column("Asset", style="cyan", no_wrap=True)
            table.add_column("Balance", style="magenta")
            table.add_column("Wallet Balance", style="green")
            
            for asset in balance:
                if float(asset['balance']) > 0:  # Only show assets with balance
                    table.add_row(
                        asset['asset'],
                        asset['balance'],
                        asset['walletBalance']
                    )
            
            console.print(table)
            
        print("\n[bold green]🎉 All tests passed! Your bot is ready to trade![/bold green]")
        return True
        
    except Exception as e:
        print(f"[bold red]❌ Test failed: {str(e)}[/bold red]")
        print("\n[yellow]🔧 Troubleshooting tips:[/yellow]")
        print("1. Check your .env file has correct API keys")
        print("2. Ensure API keys have futures trading permissions")
        print("3. Verify you're using TESTNET keys (not mainnet)")
        print("4. Check your internet connection")
        return False

def test_market_data():
    """Test market data access"""
    try:
        print("\n[bold blue]📊 Testing Market Data Access...[/bold blue]")
        bot = BasicBot()
        
        # Test symbol info
        print("[yellow]⏳ Getting BTCUSDT info...[/yellow]")
        symbol_info = bot.client.futures_exchange_info()
        
        # Test current price
        ticker = bot.client.futures_symbol_ticker(symbol="BTCUSDT")
        print(f"[green]✅ BTCUSDT Price: ${float(ticker['price']):,.2f}[/green]")
        
        return True
        
    except Exception as e:
        print(f"[red]❌ Market data test failed: {str(e)}[/red]")
        return False

if __name__ == "__main__":
    # Run connection test
    connection_ok = test_connection()
    
    if connection_ok:
        # Run market data test
        test_market_data()
        
        print("\n[bold cyan]🎯 Ready to test trading! Run: python cli.py[/bold cyan]")
    else:
        print("\n[bold red]⚠️  Fix connection issues before proceeding[/bold red]")