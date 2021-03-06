from enum import Enum

class EnvStatus(Enum):
    RUNNING, FIRED, CLEAN, TLE = range(4) 

def agent_maker(c, env, tag):
    return lambda: c(env=env, tag=tag)

def generate(maker, sz, current):
    if current is None or len(current) != sz:
        return [maker() for _ in range(sz)]
    return current
    