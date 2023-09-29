import os
from neuronexus import IPProxyPool
from playwright.async_api import async_playwright
import asyncio
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("PROXY_POOL_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("PROXY_POOL_AWS_SECRET_ACCESS_KEY")

WEBSITE = "https://ipchicken.com"

async def main():
    async with IPProxyPool(
        WEBSITE,
        key_id=AWS_ACCESS_KEY_ID,
        key_secret=AWS_SECRET_ACCESS_KEY,
        regions=["us-east-1"],
        verbose=True,
    ) as session:
        response = await session.get(WEBSITE)
        # Get the endpoint URL, assuming this is how the lib returns it
        proxy_endpoint = response.url

        print("Proxy endpoint for Playwright:", proxy_endpoint)

        # Use asynchronous Playwright API
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            # Make Playwright visit the endpoint URL
            await page.goto(str(proxy_endpoint))

            # Do other tasks...
            await page.screenshot(path="./example.png")
            await browser.close()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
