#### Download Claude Desktop
https://claude.com/download

#### Download npm
https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

#### Install UV
https://docs.astral.sh/uv/getting-started/installation/

#### Create OpenAPI Key
https://platform.openai.com/settings/organization/general

#### MCP servers list
https://github.com/modelcontextprotocol/servers?tab=readme-ov-file

#### Initiate new project
uv init HelloWorld

#### Create vrtual env
uv venv

#### Activate virtual env
source .venv/bin/activate

#### Add mcp cli
uv add "mcp[cli]"

#### To run locally for testing
mcp dev weather.py

#### Add below to Claude --> Developer Tools --> Edit Config
```{
  "mcpServers": {
    "weather": {
      "command": "/Users/manu/anaconda3/bin/uv",
      "args": [
        "--directory",
        "/Users/manu/Documents/MyApplications/Python/MCP/HELLO",
        "run",
        "python",
        "weather.py"
      ]
    }
  }
}
```

#### Another way to run:
mcp install weather.py
> This will automatically add the required commands to the config file

#### To run Client
uv run client.py