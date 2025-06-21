#!/usr/bin/env python3
"""
Debug script to see the actual balance structure
"""

from bot import BasicBot
from rich import print
import json

def debug_balance():
    """Debug the balance structure"""
    try:
        print("[bold blue]🔍 Debugging Balance Structure...[/bold blue]\n")
        
        bot = BasicBot()
        balance = bot.get_balance()
        
        if balance:
            print("[green]✅ Balance data retrieved![/green]\n")
            
            # Show the first balance item structure
            if len(balance) > 0:
                print("[yellow]📋 First balance item structure:[/yellow]")
                first_item = balance[0]
                print(json.dumps(first_item, indent=2))
                
                print(f"\n[cyan]🔑 Available keys: {list(first_item.keys())}[/cyan]\n")
            
            # Show all balances with available keys
            print("[yellow]💰 All balances:[/yellow]")
            for i, asset in enumerate(balance):
                if float(asset['balance']) > 0:
                    print(f"[green]{i+1}. {asset['asset']}: {asset['balance']}[/green]")
                    # Show all available fields for this asset
                    for key, value in asset.items():
                        if key != 'asset':
                            print(f"   {key}: {value}")
                    print()
        
        print("[bold green]✅ Debug complete![/bold green]")
        
    except Exception as e:
        print(f"[bold red]❌ Debug failed: {str(e)}[/bold red]")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_balance()