import asyncio
import requests


class ModelSelector:

    def __init__(self):
        # create request header
        self.headers = {'User-Agent': "rohith.mandavilli@gmail.com"}

        # get all companies data
        _ = requests.get(
            "",
            headers=self.headers
        )

        print("...retrieved model data...")

async def main():
    screener = ModelSelector()
    while True:
        user_input = input("Enter params? ")
        if user_input.lower() == 'exit':
            break

        print('Model Analysis:')


if __name__ == '__main__':
    asyncio.run(main())
