import json
 
PLAYER = '\u1330'
USE = 'e'
EMPTY = ''
FLOOR = '_'
EXIT = 'x'
DOOR = 'd'
SECRET = 's'
WALL = '*'
ITEMS = 'i'
STARTING_LOCATION = 'start'
playerPos = [0,0]
revealedSecret = []
doorOpen = []
inventory = []
run = True
 
def load_map(map_file_name):
    """
    When a map file name is passed the file will load the grid and return it.
    Should you modify this function? No you shouldn't.
 
    :param map_file_name: a string representing the file name.
    :return: a 2D list which contains the current map.
    """
    with open(map_file_name) as map_file:
        the_map = json.loads(map_file.read())
 
    return the_map

def isInMap(x, y, lMapX, lMpaY):
    if x >= 0 and x < lMapX and y >= 0 and y < lMpaY:
        return True
    return False

 
def lost_and_found(the_grid):

    revealedSecretCount = 0
    doorOpenCount = 0
    all_items = []
    for row_index in range(len(the_grid)):
        for col_index in range(len(the_grid[row_index])):
            if row_index == playerPos[1] and col_index == playerPos[0]:
                print(PLAYER, end=' ')
            elif the_grid[row_index][col_index]['items']:
                print(ITEMS, end=' ')
                for item in the_grid[row_index][col_index]['items']:
                    all_items.append(item)
            else:
                if the_grid[row_index][col_index]['symbol'] == SECRET:
                    if revealedSecret[revealedSecretCount]:
                        the_grid[row_index][col_index]['symbol'] = FLOOR
                        print(the_grid[row_index][col_index]['symbol'], end=' ')
                    else:
                        print(WALL, end=' ')
                    revealedSecretCount += 1
                elif the_grid[row_index][col_index]['symbol'] == DOOR:
                    #print("DOOR OPEN COUNT:" + str(doorOpenCount) + "---" + str(len(doorOpen)))
                    if doorOpen[doorOpenCount]:
                        the_grid[row_index][col_index]['symbol'] = FLOOR
                        doorOpen[doorOpenCount] = True
                    else:
                        doorOpenCount += 1

                    print(the_grid[row_index][col_index]['symbol'], end=' ')
                    
                else:
                    print(the_grid[row_index][col_index]['symbol'], end=' ')
        print()
    print(', '.join(all_items))
    action = input("Action (zqsd to move), f to open doors ans secrets: ")
    if action == 'z' and playerPos[1]-1 >= 0:
        if the_grid[playerPos[1]-1][playerPos[0]]['symbol'] == FLOOR:
            playerPos[1] -= 1
        if the_grid[playerPos[1]-1][playerPos[0]]['symbol'] == EXIT:
            return False
    elif action == 's' and playerPos[1]+1 <= len(the_grid[row_index])-1:
        if the_grid[playerPos[1]+1][playerPos[0]]['symbol'] == FLOOR:
            playerPos[1] += 1
        if the_grid[playerPos[1]+1][playerPos[0]]['symbol'] == EXIT:
            return False
    elif action == 'q' and playerPos[0]-1 >= 0:
        if the_grid[playerPos[1]][playerPos[0]-1]['symbol'] == FLOOR:
            playerPos[0] -= 1
        if the_grid[playerPos[1]][playerPos[0]-1]['symbol'] == EXIT:
            return False
    elif action == 'd' and playerPos[0]+1 <= len(the_grid[col_index])-1:
        if the_grid[playerPos[1]][playerPos[0]+1]['symbol'] == FLOOR:
            playerPos[0] += 1
        if the_grid[playerPos[1]][playerPos[0]+1]['symbol'] == EXIT:
            return False
    elif action == 'f': #open door or shearch secret
        if isInMap(playerPos[1]+1, playerPos[0], len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]+1][playerPos[0]]['symbol'] == SECRET:
                the_grid[playerPos[1]+1][playerPos[0]]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]+1][playerPos[0]]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]+1][playerPos[0]]:
                    if ''.join(the_grid[playerPos[1]+1][playerPos[0]]['requires']) in inventory:
                        the_grid[playerPos[1]+1][playerPos[0]]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]+1][playerPos[0]]['requires'])
                else:
                    the_grid[playerPos[1]+1][playerPos[0]]['symbol'] = FLOOR
        if isInMap(playerPos[1]-1, playerPos[0], len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]-1][playerPos[0]]['symbol'] == SECRET:
                the_grid[playerPos[1]-1][playerPos[0]]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]-1][playerPos[0]]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]-1][playerPos[0]]:
                    if ''.join(the_grid[playerPos[1]-1][playerPos[0]]['requires']) in inventory:
                        the_grid[playerPos[1]-1][playerPos[0]]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]-1][playerPos[0]]['requires'])
                else:
                    the_grid[playerPos[1]-1][playerPos[0]]['symbol'] = FLOOR
                
        if isInMap(playerPos[1], playerPos[0]+1, len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]][playerPos[0]+1]['symbol'] == SECRET:
                the_grid[playerPos[1]][playerPos[0]+1]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]][playerPos[0]+1]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]][playerPos[0]+1]:
                    if ''.join(the_grid[playerPos[1]][playerPos[0]+1]['requires']) in inventory:
                        the_grid[playerPos[1]][playerPos[0]+1]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]][playerPos[0]+1]['requires'])
                else:
                    the_grid[playerPos[1]][playerPos[0]+1]['symbol'] = FLOOR
                    
        if isInMap(playerPos[1], playerPos[0]-1, len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]][playerPos[0]-1]['symbol'] == SECRET:
                the_grid[playerPos[1]][playerPos[0]-1]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]][playerPos[0]-1]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]][playerPos[0]-1]:
                    if ''.join(the_grid[playerPos[1]][playerPos[0]-1]['requires']) in inventory:
                        the_grid[playerPos[1]][playerPos[0]-1]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]][playerPos[0]-1]['requires'])
                else:
                    the_grid[playerPos[1]][playerPos[0]-1]['symbol'] = FLOOR
        if isInMap(playerPos[1]+1, playerPos[0]+1, len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]+1][playerPos[0]+1]['symbol'] == SECRET:
                the_grid[playerPos[1]+1][playerPos[0]+1]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]+1][playerPos[0]+1]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]+1][playerPos[0]+1]:
                    if ''.join(the_grid[playerPos[1]+1][playerPos[0]+1]['requires']) in inventory:
                        the_grid[playerPos[1]+1][playerPos[0]+1]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]+1][playerPos[0]+1]['requires'])
                else:
                    the_grid[playerPos[1]+1][playerPos[0]+1]['symbol'] = FLOOR
        if isInMap(playerPos[1]+1, playerPos[0]-1, len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]+1][playerPos[0]-1]['symbol'] == SECRET:
                the_grid[playerPos[1]+1][playerPos[0]-1]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]+1][playerPos[0]-1]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]+1][playerPos[0]-1]:
                    if ''.join(the_grid[playerPos[1]+1][playerPos[0]-1]['requires']) in inventory:
                        the_grid[playerPos[1]+1][playerPos[0]-1]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]+1][playerPos[0]-1]['requires'])
                else:
                    the_grid[playerPos[1]+1][playerPos[0]-1]['symbol'] = FLOOR
                
        if isInMap(playerPos[1]-1, playerPos[0]+1, len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]-1][playerPos[0]+1]['symbol'] == SECRET:
                the_grid[playerPos[1]-1][playerPos[0]+1]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]-1][playerPos[0]+1]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]-1][playerPos[0]+1]:
                    if ''.join(the_grid[playerPos[1]-1][playerPos[0]+1]['requires']) in inventory:
                        the_grid[playerPos[1]-1][playerPos[0]+1]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]-1][playerPos[0]+1]['requires'])
                else:
                    the_grid[playerPos[1]-1][playerPos[0]+1]['symbol'] = FLOOR
                
        if isInMap(playerPos[1]-1, playerPos[0]-1, len(the_grid[row_index]), len(the_grid[col_index])):
            if the_grid[playerPos[1]-1][playerPos[0]-1]['symbol'] == SECRET:
                the_grid[playerPos[1]-1][playerPos[0]-1]['symbol'] = FLOOR
                print("SECRET REVEALED")
            if the_grid[playerPos[1]-1][playerPos[0]-1]['symbol'] == DOOR:
                if "requires" in the_grid[playerPos[1]-1][playerPos[0]-1]:
                    if ''.join(the_grid[playerPos[1]-1][playerPos[0]-1]['requires']) in inventory:
                        the_grid[playerPos[1]-1][playerPos[0]-1]['symbol'] = FLOOR
                    else:
                        print(the_grid[playerPos[1]-1][playerPos[0]-1]['requires'])
                else:
                    the_grid[playerPos[1]-1][playerPos[0]-1]['symbol'] = FLOOR

    if ''.join(the_grid[playerPos[1]][playerPos[0]]['items']) != '':
        inventory.append(''.join(the_grid[playerPos[1]][playerPos[0]]['items']))
        the_grid[playerPos[1]][playerPos[0]]['items'] = []
        the_grid[playerPos[1]][playerPos[0]]['symbol'] = FLOOR
    print("inventory:", end=' ')
    print(inventory)
    return True
    
if __name__ == '__main__':
    map_file_name = input('What map do you want to load? ')
    the_game_map = load_map(map_file_name)
    if the_game_map:
        # call your function now with the_game_map as a parameter.

        for row_index in range(len(the_game_map)):
            for col_index in range(len(the_game_map[row_index])):
                if the_game_map[row_index][col_index]['symbol'] == SECRET:
                    revealedSecret.append(False)
                    #print(row_index, col_index) #debug secret pos
                elif the_game_map[row_index][col_index]['symbol'] == DOOR:
                    doorOpen.append(False)

        while run:
            run = lost_and_found(the_game_map)
        print("Win !")








