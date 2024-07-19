import os
os.getcwd()
os.chdir('../Head First Python/chapter6')

''' 繼承內置的list類 '''
class AthleteList(list): 
    def __init__(self, a_name, a_birthday=None, a_time=[]):
        list.__init__([])
        self.name = a_name,
        self.birthday = a_birthday,
        self.extend(a_time) #數據本身是計時數據，所以不需要times屬性

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
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])
        
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
        return(AthleteList(tem.pop(0),tem.pop(0),tem)) #傳入Athlete後name, birth變tuple
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
james.append('1.40')
print(james.name[0]+ "'s fastest times are: "+ str(james.top3()))

