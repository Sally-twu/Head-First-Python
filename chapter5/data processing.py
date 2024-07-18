import os
os.getcwd()
os.chdir('../Head First Python/chapter5')

def get_coach_data(filename):
    new_player = []
    try:
        with open('player/'+filename) as f:
            data = f.readline()
        player = data.strip().split(',')
        ''' 使用列表推導取代重複地創建列表與迭代
        for each_item in player:
            each_item = sanitize(each_item)
            new_player.append(each_item)'''
        new_player = sorted(set([sanitize(each_item) for each_item in player]))
        return(new_player)
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins+'.'+secs)
'''用集合刪除重複項，集合的特色是無序且不允許重複項
def unique_james(james):
    clean_james = []
    for each_item in james:
        if each_item not in clean_james:
            clean_james.append(each_item)
    return(clean_james)'''

print(get_coach_data('james.txt')[0:3])
print(get_coach_data('julie.txt')[0:3])
print(get_coach_data('mikey.txt')[0:3])
print(get_coach_data('sarah.txt')[0:3])
