# Copyright 2021 John Reese
# Licensed under the MIT License

import asyncio
import shlex
import shutil
from asyncio.subprocess import PIPE
from dataclasses import dataclass
from typing import Any, Generator, List, Sequence

from .types import Config, Job, Result


def which(name: str, config: Config) -> str:
    binary = shutil.which(name)
    if binary is None:
        return name
    return binary


def render_command(run: str, config: Config) -> Sequence[str]:
    run = run.format(**config.values)
    cmd = shlex.split(run)
    cmd[0] = which(cmd[0], config)
    return cmd


@dataclass
class Step:
    cmd: Sequence[str]
    config: Config

    def __await__(self) -> Generator[Any, None, Result]:
        return self.run().__await__()

    async def run(self) -> Result:
        proc = await asyncio.create_subprocess_exec(*self.cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = await proc.communicate()
        assert proc.returncode is not None

        return Result(
            command=self.cmd,
            exit_code=proc.returncode,
            stdout=stdout.decode(),
            stderr=stderr.decode(),
        )


def prepare_job(job: Job, config: Config) -> Sequence[Step]:
    tasks: List[Step] = []

    for item in job.run:
        cmd = render_command(item, config)
        tasks.append(Step(cmd=cmd, config=config))

    return tasks
