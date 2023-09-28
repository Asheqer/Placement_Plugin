import json
import quart
import quart_cors
from quart import request

# Note: Setting CORS to allow chat.openapi.com is only required when running a localhost plugin
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
HOST_URL = "https://example.com"

@app.get("/placements")
async def get_placements():
    query = request.args.get("query")
    res = request.args.get(f"{HOST_URL}/api/v1/get_placements?search={query}&page=0&per_page=100")
    body = res.json()