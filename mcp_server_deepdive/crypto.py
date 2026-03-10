from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Crypto")

@mcp.tool()
def get_crypto_price(crypto: str) -> str:
    """
    Fetches the current price of the specified cryptocurrency.
    Args:
        crypto (str): The symbol of the cryptocurrency (e.g., "BTC" for Bitcoin, "ETH" for Ethereum).
    Returns:
        str: The current price of the cryptocurrency in USD or an error message if the price cannot be fetched.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto.lower(),
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException:
        return f"Failed to retrieve price for {crypto}. Could not connect to API."
    if response.status_code == 200:
        data = response.json()
        if crypto in data:
            return f"The current price of {crypto} is ${data[crypto].get('usd')}."
        else:
            return f"{crypto} not found."
    else:
        return f"Failed to retrieve price for {crypto}. Status code: {response.status_code}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
