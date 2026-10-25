import asyncio
import traceback
from telethon import TelegramClient

# Fake credentials only: handshake test, no login, no real secrets.
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'


async def main():
    print('START mtproto handshake test', flush=True)
    client = TelegramClient('mtproto-test-session', API_ID, API_HASH)
    try:
        await asyncio.wait_for(client.connect(), timeout=30)
        print(f"connected={client.is_connected()}", flush=True)
    except Exception as e:
        print(f"connected=False error={type(e).__name__}: {e}", flush=True)
        traceback.print_exc()
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass
    print('DONE', flush=True)


if __name__ == '__main__':
    asyncio.run(main())
