import json
 
USE = 'e'
FLOOR = '_'
EXIT = 'X'
DOOR = 'D'
SECRET = 'S'
MONSTER_SYMBOL = 'M'
WALL = '*'
NEWLINE = '\n'
 
 
def valid_position(y, x, the_map):
    if 0 <= y < len(the_map) and 0 <= x < len(the_map[y]):
        return True
    return False
 
 
def modify_map(map_to_mod):
    s = input('Select position or quit: ')
    while s != 'quit':
        try:
            y, x = [int(x) for x in s.split()]
            if valid_position(y, x, map_to_mod):
                in_str = input('What do you want to do (add item)? Add requirement? ')
                command = in_str.split()[0]
                item_name = ' '.join(in_str.split()[1:])
                if command == 'add-item':
                    if item_name not in map_to_mod[y][x]['items']:
                        map_to_mod[y][x]['items'].append(item_name)
                elif command == 'add-requirement' and map_to_mod[y][x]['symbol'].upper() in [DOOR, SECRET]:
                    if 'requires' in map_to_mod[y][x] and item_name not in map_to_mod[y][x]['requires']:
                        map_to_mod[y][x]['requires'].append(item_name)
                    elif 'requires' not in map_to_mod[y][x]:
                        map_to_mod[y][x]['requires'] = [item_name]
                elif command == 'remove-requirement' and map_to_mod[y][x]['symbol'].upper() in [DOOR, SECRET]:
                    if 'requires' in map_to_mod[y][x] and item_name in map_to_mod[y][x]['requires']:
                        map_to_mod[y][x]['requires'].remove(item_name)
                elif command == 'remove-item':
                    while item_name in map_to_mod[y][x]['items']:
                        map_to_mod[y][x]['items'].remove(item_name)
                elif command == 'add-start':
                    map_to_mod[y][x]['start'] = True
                else:
                    print(f'Unknown command {command}')
        except ValueError:
            print('You must enter two integers separated by a space.')
 
        s = input('Select position or quit: ')
 
 
if __name__ == '__main__':
    cols = 0
    try:
        rows, cols = [int(x) for x in input('How many rows and cols will your map be? ').split()]
        file_name = input('What file do you want to create and then modify to add "s" for secrets "d" for doors, "x" for exit, "*" for walls "_" or space for floors: ')
        with open(file_name + '.premap', 'w') as the_pre_map_file:
            map_line = ''.join([FLOOR] * cols) + NEWLINE
            for _ in range(rows):
                the_pre_map_file.writelines(map_line)
    except ValueError:
        file_name = input('What file do you want to modify to add "s" for secrets "d" for doors, "x" for exit, "*" for walls "_" or space for floors: ')
 
    input('Go and modify the file with the walls, exits, doors and secrets, press enter key to continue... ')
 
    the_map = []
 
    with open(file_name + '.premap', 'r') as the_pre_map_file:
        if cols == 0:
            cols = int(input('How many columns are there? '))
        print(' ' + ''.join([str(x).ljust(4) for x in range(cols)]))
        for i, line in enumerate(the_pre_map_file):
            print(i, '   '.join(list(line.strip())))
            the_map.append(list({'symbol': x, 'items': []} for x in line.strip()))
 
    modify_map(the_map)
 
    print(the_map)
    with open(file_name + '.map', 'w') as map_file:
        map_file.write(json.dumps(the_map, indent='\t'))

