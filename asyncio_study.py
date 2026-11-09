import asyncio
import time
import requests

# ---- 并发限流：最多同时 2 个请求 ----
SEM = asyncio.Semaphore(2)

# ---- 速率限流：令牌桶，每秒最多 1 个请求 ----
class RateLimiter:
    def __init__(self, rate: float):
        self.interval = 1 / rate
        self._last = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            wait = self._last + self.interval - time.monotonic()
            if wait > 0:
                await asyncio.sleep(wait)
            self._last = time.monotonic()

LIMITER = RateLimiter(rate=1)  # 1 QPS

async def fetch_url(url: str, timeout: float = 5.0):
    async with SEM:                       # 并发限流
        await LIMITER.acquire()           # 速率限流
        try:
            async with asyncio.timeout(timeout):   # 单请求超时，3.11+
                print(f"开始同步抓取 {url}...")
                response = await asyncio.to_thread(requests.get, url)
            print(f"完成 {url}，状态码: {response.status_code}")
            return len(response.content)
        except TimeoutError:
            print(f"超时: {url}")
            return None
        except Exception as e:
            print(f"失败: {url} -> {e!r}")
            return None

async def main():
    urls = [
        "https://www.example.com",
        "https://www.baidu.com",
        "https://www.bing.com",
    ]
    results = await asyncio.gather(*(fetch_url(u) for u in urls))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())