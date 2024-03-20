#Importing lib python
import aiohttp
import asyncio
import time

# in discord Hold CTRL + SHIFT + I
# url Text Channel = Network -> Headers -> General -> Request URL
url = ""

headers = {
    "Content-Type": "application/json",

    # Network -> Headers -> Request Headers -> 8(Authorization) (Need Key discord Personal)
    "Authorization": "",
}

async def fetch_message(session, url):
    start_time = time.time()
    async with session.get(url, headers=headers, params={"limit": 1}) as response:
        end_time = time.time()
        return await response.json(), end_time - start_time

async def main():
    urls = [""] 
    connector = aiohttp.TCPConnector(limit=None)

    async with aiohttp.ClientSession(connector=connector) as session:
        while True:
            try:
                tasks = [fetch_message(session, url) for url in urls]
                results = await asyncio.gather(*tasks)

                for message, ping_time in results:
                    content = message[0].get("content", "")
                    
                    # Network -> Payload -> content
                    if "" in content:
                        reply_payload = {
                            "content": "Take",
                            "tts": False,
                        }
                        async with session.post(url, json=reply_payload, headers=headers) as response:
                            ping_ms = int(ping_time * 1000)
                            print(f"(Ping Time: {ping_ms} ms)")

            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
