import argparse
import time
start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', type=str, required=True)
parser.add_argument('--red', type=int, required=True)
parser.add_argument('--green', type=int, required=True)
parser.add_argument('--blue', type=int, required=True)
parser.add_argument('-v', '--verbose', required=False, action='store_true')

args = parser.parse_args()
inputfile = args.file
red = args.red
green = args.green
blue = args.blue
verbose = args.verbose
with open(inputfile, 'r') as f:
    inpt = f.read()

"""
      # Day 2: Code Conundrum
      # input: 12 red cubes, 13 green cubes, 14 blue cubes

"""

if verbose:
    print(
        f'On input file {inputfile} calculating Day 2 result with Red: {red}, Green: {green} and Blue: {blue}')


# Part 1
def d2_cube_conundrum_p1(inpt: str) -> list:
    result = set()
    for i, v in enumerate(inpt.split('\n')[:-1]):
        games = v.split(': ')[-1]
        gameLen = len(games.split('; '))
        for ga in games.split('; '):
            gc = {'blue': 0, 'green': 0, 'red': 0}
            for g in ga.split(', '):
                # if verbose:
                #     print(g)
                if g.split(' ')[1] == 'blue':
                    gc['blue'] = int(g.split(' ')[0])
                if g.split(' ')[1] == 'green':
                    gc['green'] = int(g.split(' ')[0])
                if g.split(' ')[1] == 'red':
                    gc['red'] = int(g.split(' ')[0])
            if verbose:
                print(gc)

            if gc['blue'] <= blue and gc['green'] <= green and gc['red'] <= red:
                result.add(i+1)
            else:
                result - {i+1}
                print(f'Removing {i+1} {gc}')
                break

        if verbose:
            print(f'{i+1} games: {games} -> gameLen: {gameLen}\n')

    return sum(result)


print(d2_cube_conundrum_p1(inpt))
# Part 2


print('------------------ %s seconds ----------------------' %
      (time.time()-start_time))
