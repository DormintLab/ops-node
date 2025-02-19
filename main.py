import argparse
import asyncio
import sys
from pathlib import Path
from dormai.async_api import AsyncDormAI


async def main():

    async with AsyncDormAI(Path("./dormai.yml")) as dormai:
        event = {}
        op_type = dormai.settings["OP_TYPE"]

        while True:
            inputs, context = await dormai.receive_event()
            if inputs is None:
                continue

            print(inputs,
                  file=sys.stderr)

            if len(event) == 2:
                await dormai.send_event(dormai.OutputData(**event),
                                        context)


if __name__ == "__main__":
    asyncio.run(main())
