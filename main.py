from src import Logger, get_env, get_robot, parse_arguments
from collections import defaultdict

def get_level(level):
    try:
        return int(level)
    except ValueError:
        return level.upper()

def main(args):
    # Setting up the app logger
    logger = Logger('App', args.log_file)
    level = get_level(args.level)
    try:
        logger.setLevel(level)
    except ValueError:
        logger.setLevel('INFO')
        logger.error(f'`{level}` is not a valid logging level, setting the level to INFO', 'main')

    # Running the env
    data = defaultdict(lambda: 0)
    env_class = get_env(args.env)
    for _ in range(args.repetitions):
        env = env_class(args.rows, args.columns, args.time, args.babies, \
            args.toys, args.dirty, args.cicles, get_robot(args.robot))
        status = env.run()
        data['DIRTY-MEAN'] += env.dirty
        data[status.name]  += 1

    # Computing the result
    logger.debug(f"Acumulated dirty amount is {data['DIRTY-MEAN']}", 'main')
    data['DIRTY-MEAN'] /= args.repetitions
    if args.verbose:
        print('\n'.join(f'{key}: {value}' for key, value in data.items()))
    return data

if __name__ == "__main__":
    parse_arguments(main)
