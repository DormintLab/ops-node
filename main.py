import asyncio
import sys
from pathlib import Path
from dormai.async_api import AsyncDormAI


async def main():

    async with AsyncDormAI(Path("./dormai.yml")) as dormai:
        event = {}
        op_type = dormai.settings["OP_TYPE"]
        print(f"OP_TYPE={op_type}", file=sys.stderr)

        while True:
            inputs, context = await dormai.receive_event()
            print(inputs,
                  file=sys.stderr)

            if inputs is None:
                continue

            if len(event) == 2:
                await dormai.send_event(dormai.OutputData(**event),
                                        context)


if __name__ == "__main__":
    asyncio.run(main())
