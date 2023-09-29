<h1 align="center">NeuroNexus</h1>
<div align="center">
    <img src="static/images/NeuroNexus.png" width="500">
</div>

<h4 align="center">Open Source Proxy Rotation Solution 🌐</h4>
<h5 align="center">Freely Scrape, and Crawl Fast and Easy ✨</h5>

<div align="center">

<a href="https://github.com/NorkzYT/NeuroNexus/graphs/contributors"><img src="https://img.shields.io/github/contributors/NorkzYT/NeuroNexus.svg" alt="Contributors"></a>
<a href="https://github.com/NorkzYT/NeuroNexus/network/members"><img src="https://img.shields.io/github/forks/NorkzYT/NeuroNexus.svg" alt="Forks"></a>
<a href="https://github.com/NorkzYT/NeuroNexus/stargazers"><img src="https://img.shields.io/github/stars/NorkzYT/NeuroNexus.svg" alt="Stargazers"></a>
<a href="https://github.com/NorkzYT/NeuroNexus/issues"><img src="https://img.shields.io/github/issues/NorkzYT/NeuroNexus.svg" alt="Issues"></a>
<a href="https://github.com/NorkzYT/NeuroNexus/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/NorkzYT/NeuroNexus.svg" alt="Closed Issues"></a>
<a href="https://github.com/NorkzYT/NeuroNexus/blob/master/LICENSE"><img src="https://img.shields.io/github/license/NorkzYT/NeuroNexus.svg" alt="MIT License"></a>

</div>

<h2 align="left">🔧 Installation</h2>

```bash
pip install NeuroNexus
```

<h2 align="left">🛠 Setup</h2>

Make an AWS account and create a new IAM user with the permission of `AmazonAPIGatewayAdministrator`. Then, to find your access key ID and secret access key, follow the [official AWS tutorial](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html).

Set up your AWS credentials in your `.env` file or with [awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) by running `aws configure`.

```env
PROXY_POOL_AWS_ACCESS_KEY_ID=your_access_key_id
PROXY_POOL_AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

<h2 align="left">📖 Usage</h2>

Example usage:

```python
import os
import asyncio
from dotenv import load_dotenv
from neuronexus import IPProxyPool

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("PROXY_POOL_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("PROXY_POOL_AWS_SECRET_ACCESS_KEY")


async def main():
    session = IPProxyPool(
        "https://api.ipify.org",
        key_id=AWS_ACCESS_KEY_ID,
        key_secret=AWS_SECRET_ACCESS_KEY,
        regions=["us-east-1"],
        verbose=True,
    )
    await session.start()
    for _ in range(5):
        response = await session.get("https://api.ipify.org")
        print(f"Your ip: {await response.text()}")
    await session.close()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
```

### Alternate Usage (Automatic Shutdown)

```python
import os
import asyncio
from dotenv import load_dotenv
from neuronexus import IPProxyPool

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("PROXY_POOL_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("PROXY_POOL_AWS_SECRET_ACCESS_KEY")

async def main():
    async with IPProxyPool(
        "https://api.ipify.org",
        key_id=AWS_ACCESS_KEY_ID,
        key_secret=AWS_SECRET_ACCESS_KEY,
        regions=["us-east-1"],
        verbose=True,
    ) as session:
        for _ in range(5):
            response = await session.get("https://api.ipify.org")
            print(f"Your ip: {await response.text()}")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
```

⚠️ Remember: If gateways are not shut down via the `shutdown()` method via method #1, you may incur charges.

<details>
  <summary>📌 Output: </summary>
  
```logs
>> Starting IP Rotating APIs in 1 regions
>> Created API with id "vg3uqmsxk8"
>> API launched in 1 regions out of 1
Your ip: 242.95.100.230
Your ip: 195.203.105.186
Your ip: 93.48.255.192
Your ip: 132.216.102.184
Your ip: 177.139.104.241
>> Deleted rest API with id "vg3uqmsxk8"
>> All created APIs for ip rotating have been deleted
```
</details>

<h2 align="left">🔎 Parameters Guide</h2>
NeuroNexus supports various parameters that you can include when initializing the API Gateway. Here's a detailed overview of all the parameters available:

&nbsp;
| Name              | Description                                          | Required    | Default
| -----------       | -----------                                          | ----------- | -----------
| site              | The site (without path) requests will be sent to.    | True        |
| regions           | An array of AWS regions to setup gateways in.        | False       | DEFAULT_REGIONS
| key_id            | AWS Access Key ID (will override env variables).     | False       | *Relies on env variables.*
| key_secret        | AWS Access Key Secret (will override env variables). | False       | *Relies on env variables.*
| verbose           | Include status and error messages.                   | False       | False

<details>
  <summary>📌 Example:</summary>

```python
from neuronexus import IPProxyPool, EXTRA_REGIONS, ALL_REGIONS

# Gateway to outbound HTTP IP and port for only two regions
gateway_1 = IPProxyPool("http://1.1.1.1:8080", regions=["eu-west-1", "eu-west-2"])

# Gateway to HTTPS google for the extra regions pack, with specified access key pair
gateway_2 = IPProxyPool("https://www.google.com", regions=EXTRA_REGIONS, key_id="ID", key_secret="SECRET")
```

</details>

<h2 align="left">🤝 Contributing</h2>

1. 🍴 Fork the repo!

2. 🔧 Make your changes.

3. 📦 Push your changes to a new branch and create a Pull Request.

Every contribution is welcome! 💖

<h2 align="left">📄 License</h2>

This project is licensed under the MIT License. For more details, see [LICENSE](https://github.com/NorkzYT/NeuroNexus/blob/master/LICENSE).
