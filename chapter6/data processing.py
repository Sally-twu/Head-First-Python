import os
os.getcwd()
os.chdir('../Head First Python/chapter6')

class Athlete:
    def __init__(self, a_name='', a_birthday='', a_time=[]):
        self.name = a_name,
        self.birthday = a_birthday,
        self.time = a_time
    
    def sanitize(self, time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins+'.'+secs)
    
    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self.time]))[0:3])
    
    def add_time(self, time_value = None):
        self.time.append(time_value)
    
    def add_times(self, list_of_times = []):
        self.time.extend(list_of_times)
        
    ''' 繼承內置的list類 '''
    class AthleteList(list):
        def __init__(self, a_name='', a_birthday='', a_time=[]):
            self.name = a_name,
            self.birthday = a_birthday,
            self.time = a_time
        
def get_coach_data(filename):
    try:
        with open('player/'+filename) as f:
            data = f.readline()
        tem = data.strip().split(',')
        ''' 
        (james_name, james_dob) = (james.pop(0),james.pop(0))
        建立字典使內存數據貼近真實數據結構，並存放在函數中使其通用化
        new_data = {
            'name':data.pop(0),
            'birthday':data.pop(0),
            'time':str(sorted(set([self.sanitize(t) for t in data]))[0:3])
        }'''
        return(Athlete(tem.pop(0),tem.pop(0),tem)) #傳入Athlete後name, birth變tuple
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
james.add_time('1.50')
print(james.name[0]+ "'s fastest times are: "+ str(james.top3()))

