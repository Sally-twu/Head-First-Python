'''導入os取得當前工作目錄並切換到包含數據文件的資料夾
逐行列印文件中內容'''
import os
import pickle
from nester import print_item
os.getcwd()
os.chdir('../Head First Python/chapter3&4')
'''使用額外邏輯處理文件I/O錯誤
if os.path.exists('sketch.txt'):'''
man = []
other = [] 
try:
    data = open('sketch.txt')
    '''在劇本中根據冒號將句子分為人物與台詞兩個部分
    有些數據行不包含冒號，有兩種處理方式: 
    一、增加額外的代碼來檢查是否可以調用split
    二、監控錯誤發生並做相應的措施'''
    '''第一種
    for each_line in the_file:
        if each_line.find(":") >0:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')'''

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

'''假設在寫入代碼的過程中出現錯誤直接執行異常處理，則文件可能無法正常關閉
故若出現不論出現甚麼錯誤都必須運行某些代碼時，可以向try語句的finally增加代碼
try:
    man_out = open("man_data.txt", "w")
    other_out = open("other_data.txt", "w")
    
    print(man, file=man_out)
    print(other, file=other_out)
except IOError as err: 
    為異常對象取名並作為錯誤消息的一部分
    可以得到一個特定的錯誤訊息，指出哪裡出問題
    print('File error: ' + str(err))
finally:
    man_out.close()
    other_out.close()
'''

'''有了with語句後就不需要finally即可妥善關閉一個可能打開的數據文件
try:
    with open("man_data.txt", "w") as man_out:
        print_item(man, fn=man_out) # 將數據輸出為更容易解析的格式
    with open("other_data.txt", "w") as other_out:
        print_item(other, fn=other_out)   
except IOError as err: 
    為異常對象取名並作為錯誤消息的一部分
    可以得到一個特定的錯誤訊息，指出哪裡出問題
    print('File error: ' + str(err))'''

'''加入pickle'''
try:
    with open('man.pickle','wb') as mandata:
        pickle.dump(man, mandata)
    with open('other.pickle','wb') as otherdata:
        pickle.dump(other, otherdata)
except IOError as err: 
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error'+ str(perr))