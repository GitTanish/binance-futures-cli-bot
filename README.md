# Binance Futures CLI Bot

A **command-line based crypto trading bot** built with Python that connects to the **Binance Futures Testnet**. This bot allows users to simulate placing trades like a real trader, but without using real money. It focuses on the **basics of trading automation** and serves as a learning tool or base for more complex bots in the future.

## 🚀 Features

- **Market Orders**: Execute immediate buy/sell orders at current market price
- **Limit Orders**: Place orders at specific price levels
- **TWAP (Time-Weighted Average Price)**: Split large orders into smaller parts executed over time
- **Testnet Trading**: Safe simulation environment with no real money at risk
- **Rich CLI Interface**: Beautiful command-line interface with colors and prompts
- **Comprehensive Logging**: All trading activities are logged to file for analysis
- **Balance Checking**: View your testnet account balance

## 📋 Prerequisites

- Python 3.7 or higher
- Binance Futures Testnet account
- API Key and Secret from Binance Testnet

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GitTanish/binance-futures-cli-bot.git
   cd binance-futures-cli-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   API_KEY=your_binance_testnet_api_key
   API_SECRET=your_binance_testnet_secret_key
   ```

4. **Get Binance Testnet API Keys**
   - Visit [Binance Futures Testnet](https://testnet.binancefuture.com/)
   - Create an account or log in
   - Generate API Key and Secret
   - Add them to your `.env` file

## 🚀 Usage

Run the bot:
```bash
python cli.py
```

### Available Order Types

1. **Market Order**: Executes immediately at current market price
2. **Limit Order**: Places order at specified price (waits for price to be reached)
3. **TWAP Order**: Splits your order into multiple smaller orders executed over time

### Example Trading Session

```
Binance Futures CLI Bot Connected

Choose an order type:
1. Market
2. Limit  
3. TWAP
4. Exit

Your choice: 1
Enter symbol [BTCUSDT]: BTCUSDT
Buy or Sell? [BUY/SELL]: BUY
Quantity: 0.001

Market Order Placed Successfully
```

## 📁 Project Structure

```
binance-futures-cli-bot/
├── bot.py          # Main bot class with Binance client
├── cli.py          # Command-line interface
├── config.py       # Configuration and environment variables
├── loggers.py      # Logging setup
├── orders.py       # Order execution functions
├── requirements.txt # Python dependencies
├── .env            # Environment variables (create this)
└── bot.log         # Trading logs (auto-generated)
```

## 🔧 Configuration

The bot uses the following configuration:

- **Testnet URL**: `https://testnet.binancefuture.com`
- **Default Symbol**: BTCUSDT
- **Log File**: `bot.log`
- **TWAP Default**: 5 intervals with 3-second delays

You can modify these settings in the respective files.

## 📊 Logging

All trading activities are automatically logged to `bot.log` with timestamps. This includes:
- Successful orders
- Error messages
- Order details and responses

## ⚠️ Important Notes

- **This bot uses TESTNET only** - No real money is involved
- Always test thoroughly before considering any real trading implementation
- This is for educational purposes and learning trading automation basics
- Never share your API keys publicly

## 🛡️ Safety Features

- **Testnet Only**: Configured to work exclusively with Binance Futures Testnet
- **Error Handling**: Comprehensive error handling for network issues and API errors
- **Logging**: All activities are logged for review and debugging

## 🔮 Future Enhancements

- Technical indicators integration
- Stop-loss and take-profit orders
- Portfolio management features
- Backtesting capabilities
- WebSocket real-time data streaming
- Advanced order types (OCO, Trailing Stop)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This software is for educational purposes only. Trading cryptocurrencies involves substantial risk of loss. The authors are not responsible for any financial losses incurred through the use of this software. Always do your own research and consider consulting with a financial advisor.

## 📞 Support

If you encounter any issues or have questions:
1. Check the `bot.log` file for error details
2. Ensure your API keys are correct and have proper permissions
3. Verify your internet connection and Binance Testnet status

---

**Happy Trading! 🚀📈**
