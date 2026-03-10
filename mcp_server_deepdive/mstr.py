from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("MSTR")

@mcp.tool()
def get_mstr_model_details() -> str:
    """
    Fetches the details on the data model from MSTR Mosaic API.
    This includes overall description of the model, the list of attributes, metrics and the description for the attributes and metrics present in the model.
    """
    baseUrl = "https://autotrial.microstrategy.com/MicroStrategyLibrary/api"
    authPayload = {"username": "", "password": "", "loginMode": 1}
    projectID = ""
    dataModelID = ""

    resp = requests.post(f"{baseUrl}/auth/login", json=authPayload, verify=False)
    authToken = resp.headers.get("X-MSTR-AuthToken")
    cookies = resp.cookies
    headers = {
        "content-Type": "application/json",
        "Accept": "application/json",
        "X-MSTR-ProjectID": projectID,
        "X-MSTR-Authtoken": authToken,
        "Connection": "keep-alive"
    }
    respModel = requests.get(f"{baseUrl}/model/dataModels/{dataModelID}", cookies=cookies, headers=headers, verify=False).json()
    respAttr = requests.get(f"{baseUrl}/model/dataModels/{dataModelID}/attributes", cookies=cookies, headers=headers, verify=False).json()
    respMetr = requests.get(f"{baseUrl}/model/dataModels/{dataModelID}/factMetrics", cookies=cookies, headers=headers, verify=False).json()
    attr_descriptions = []
    for attr in respAttr["attributes"]:
        attr_descriptions.append(attr["information"]["name"] + " : " + attr["information"]["description"])
    met_descriptions = []
    for met in respMetr["factMetrics"]:
        met_descriptions.append(met["information"]["name"] + " : " + met["information"]["description"])
    
    finalData = {
        "modelDetails": respModel,
        "attributeDescriptions": attr_descriptions,
        "metricDescriptions": met_descriptions
    }
    return str(finalData)

if __name__ == "__main__":
    mcp.run(transport="stdio")