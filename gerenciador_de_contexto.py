import asyncio

class AsyncContexto:
    async def __aenter__(self):
        print("Entrando no async with...")
        await asyncio.sleep(1)
        return "valor"

    async def __aexit__(self, exc_type, exc, tb):
        print("Saindo no async with...")
        await asyncio.sleep(1)
        if exc:
            print("Erro detectado:", exc)
        return False

