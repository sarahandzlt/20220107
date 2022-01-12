# 写个测试程序
import voting
from voting import harmonic, scoringRule, plurality, STV, generatePreferences
import openpyxl

def main():
    #test openpyxl
    path = "voting.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    varexcel = generatePreferences(sheet_obj)
# {1: [1, 2, 3, 4, 5, 6],
#2: [4, 5, 1, 3, 2, 6],
#3: [6, 1, 2, 3, 4, 5],
#4: [5, 3, 2, 1, 4, 6],
#5: [1, 3, 2, 4, 5, 6],
#6: [3, 2, 4, 6, 5, 1],
#7: [3, 1, 4, 5, 6, 2],
#8: [1, 3, 2, 5, 6, 4],
#9: [1, 6, 4, 5, 3, 2],
#10: [6, 3, 2, 4, 5, 1]}
    #6
    dict = {}
    dict[1] = [1, 2, 3, 4, 5, 6]
    dict[2] = [4, 5, 1, 3, 2, 6]
    dict[3] = [6, 1, 2, 3, 4, 5]
    dict[4] = [5, 3, 2, 1, 4, 6]
    dict[5] = [1, 3, 2, 4, 5, 6]
    dict[6] = [3, 2, 4, 6, 5, 1]
    dict[7] = [3, 1, 4, 5, 6, 2]
    dict[8] = [1, 3, 2, 5, 6, 4]
    dict[9] = [1, 6, 4, 5, 3, 2]
    dict[10] = [6, 3, 2, 4, 5, 1]

    # 还是一样，有入参出参就可以做个测试方法
    #harmonic(dict, 6)
    #{1: [1, 2, 3, 4, 5, 6], 2: [4, 5, 1, 3, 2, 6], 3: [6, 1, 2, 3, 4, 5], 4: [5, 3, 2, 1, 4, 6], 5: [1, 3, 2, 4, 5, 6],
    # 6: [3, 2, 4, 6, 5, 1], 7: [3, 1, 4, 5, 6, 2], 8: [1, 3, 2, 5, 6, 4], 9: [1, 6, 4, 5, 3, 2], 10: [6, 3, 2, 4, 5, 1]}
   #borda(dict, 'max')
    dict = {1: [1, 2, 3, 4, 5, 6], 2: [4, 5, 1, 3, 2, 6], 3: [6, 1, 2, 3, 4, 5], 4: [5, 3, 2, 1, 4, 6],
            5: [1, 3, 2, 4, 5, 6], 6: [3, 2, 4, 6, 5, 1], 7: [3, 1, 4, 5, 6, 2], 8: [1, 3, 2, 5, 6, 4],
            9: [1, 6, 4, 5, 3, 2], 10: [6, 3, 2, 4, 5, 1]}
    varresult = STV(dict, 'max')
    print("varresult::  " + str(varresult))
    pass
    #scoringRule(None, [10,2,2,2,2,2], 4)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


