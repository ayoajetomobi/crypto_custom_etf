# Disclaimer

This strategy and the accompanying code are provided by Lumiwealth for educational purposes only. They are not intended for use with real money nor should they be construed as investment advice. The tools are designed for financial analysis and should not form the sole basis of any investment decisions. Please be aware that Lumiwealth is not a licensed investment advisor.

1. Hypothetical Performance: Any backtesting results presented are hypothetical and do not represent actual trading. Past performance is not indicative of future results. There is no guarantee that the strategy will perform similarly in the future, nor is there any assurance of profitability.

2. User Risk: The strategy and code may not be suitable for your specific financial situation and risk tolerance. It is crucial to consult with a qualified financial professional before making any investment decisions.

3. Code Warranty: The code is provided 'as is' without any warranty. While efforts have been made to ensure its correctness, Lumiwealth does not guarantee that the code is free from bugs or errors.

4. Information Accuracy: All accompanying information, including strategy descriptions, backtests, etc., is provided without warranty and may be subject to errors or inaccuracies. Lumiwealth reserves the right to make changes to the code and information at any time without notice.

5. Intellectual Property: The code, along with any documentation or related materials, is the proprietary property of Lumiwealth. Unauthorized copying, distribution, or resale of the code is strictly prohibited. Users must delete all copies of the code upon termination of their subscription or service agreement with Lumiwealth.

6. License: For detailed licensing information, please refer to the [license](LICENSE).

7. Scope of Agreement: This disclaimer is specific to the strategy and code in question and does not supersede the broader Terms of Service agreed upon during the Lumiwealth signup process. It is an integral part of the larger legal framework governing your use of Lumiwealth's services.

By using this strategy and code, you acknowledge and agree to the terms outlined in this disclaimer, which form part of the agreement between you and Lumiwealth. Your agreement to these terms, as part of your use of the strategy and code, is acknowledged by your continued use of Lumiwealth's services.

# Strategy Description

This strategy will rebalance a portfolio of crypto assets every X days. The portfolio is defined in the parameters
section of the strategy. The portfolio is a list of assets, each with a symbol, a weight, and a quote asset. The
quote asset is the asset that the symbol is quoted in. For example, if you want to trade BTC/USDT, then the quote
asset is USDT. If you want to trade BTC/USD, then the quote asset is USD. The quote asset is used to calculate
the value of the portfolio. The weight is the percentage of the portfolio that the asset should take up. For example,
if you have 3 assets in your portfolio, each with a weight of 0.33, then each asset will take up 33% of the portfolio.


# Getting Started

To run this strategy on Replit or Render, click on the buttons below. This will open the strategy on the respective platform. You can then follow the instructions in the [Deployment Guide](https://lumibot.lumiwealth.com/deployment.html) to set up the strategy.
 
### TIP: Right click on the button and open it in a new tab so that you can see the instructions while you are setting up the strategy (otherwise you will have to press the back button to see the instructions again).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Lumiwealth-Strategies/stock_example_algo)

[![Run on Repl.it](https://replit.com/badge/github/Lumiwealth-Strategies/stock_example_algo)](https://replit.com/new/github/Lumiwealth-Strategies/stock_example_algo)

# How to Run the Strategy

The full guide on how to run the strategy is available in the [Deployment Guide](https://lumibot.lumiwealth.com/deployment.html).

[Click here for instructions](https://lumibot.lumiwealth.com/deployment.html)

To get your bot live and trading, follow these quick steps:

1.	Choose Your Platform: We recommend deploying on either Render or Replit for ease and affordability.
•	[Deploy on Render](https://lumibot.lumiwealth.com/deployment.html#deploying-to-render)
•	[Deploy on Replit](https://lumibot.lumiwealth.com/deployment.html#deploying-to-replit)
2.	Configure Your Secrets: Set up your environment variables (e.g., API keys) and broker-specific settings by adding them to the secrets tab. Here's the section on [how to set up secrets](https://lumibot.lumiwealth.com/deployment.html#secrets-configuration).
3.	Deploy & Monitor: Follow our detailed instructions for Render or Replit, and once your bot is live, monitor its performance through your broker account. You can also check the logs on the deployment platform for any errors or warnings.

# Secrets Configuration

The strategy can be configured by setting the following secrets in the replit secrets tab. Inside replit, just open the secrets tab (under tools) and click "New secret" to add a new secret. The secret key should be the name of the secret (from the left column in the table below) and the secret value should be the value of the secret depending on your situation (example values are given in the right column in the table below).

If you are running the strategy on your own computer, you can set these as environment variables.

| Secret            | Description                                                                                   | Example                                 |
|-------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------|
| COINBASE_API_KEY  | Your Coinbase API Key                                                                         | 341JGHJLis6dLErR4                         |
| COINBASE_API_SECRET | Your Coinbase API Secret                                                                     | 9WgJLS3wI3q54FCpLwwZjCp8JCfJfKuwSrYskPMA |
| ALPACA_API_KEY    | **(Optional)** Your API key from your Alpaca brokerage account                                               | PK7T6YVAX6PMH1EM20YN                    |
| ALPACA_API_SECRET | **(Optional)** Your secret key from your Alpaca brokerage account                                            | 9WgJLS3wIXq54FCpHwwZjCp8JCfJfKuwSrYskKMA |
| ALPACA_IS_PAPER   | **(Optional)** Set to "True" to use the Alpaca paper trading API, set to "False" to use the Alpaca real money trading API (defaults to True) | True                                  |
| IS_BACKTESTING    | **(Optional)** Set to "True" to run the strategy in backtesting mode, set to "False" to run the strategy live (defaults to False) | False                                  |
| POLYGON_API_KEY   | **(Optional)** Your API key from your Polygon account, only needed if you are backtesting                    | a7py0zIdhxde6QkX8OjjKNp7cD87hwKU        |

# Modifying the Parameters

The strategy parameters can be modified by editing the "parameters" section of the `main.py` file, usually near the top of the file just under the `class` definition. It is a python dictionary that looks like this:

```python
parameters = {
    "my_parameter_1": 1,
    ...
}
```

You can change the values of the parameters by editing the numbers in the dictionary. For example, if you wanted to change the value of "my_parameter_1" to 2, you would change the code to look like this:

```python
parameters = {
    "my_parameter_1": 2,
    ...
}
```

Each parameter controls a different aspect of the strategy, and the description of each parameter is given next to the parameter in the code. Changing the parameters can have a big effect on the performance of the strategy, so it is recommended that you backtest the strategy after changing the parameters to see how it would have performed.

# Backtest

This is a backtest of the strategy using the current parameters in the code. Remember that past performance is not indicative of future results and there is no guarantee that the backtest was performed correctly or that the strategy will perform without errors when run live.

![Tearsheet generated by QuantStats](Tearsheet%20(generated%20by%20QuantStats).jpg)

