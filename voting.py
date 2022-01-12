def generatePreferences(values):
    print("generatePreferences")
    print(values)
    dict = {}

    for i in range(values.max_row):
        list1 = []
        for j in range(values.max_column):
            cell = values.cell(row=i + 1, column=j + 1).value
            list1.append({'index': j + 1, 'value': cell})

            # sorted_list = [item['index'] for item in list2]

        # for j in range(0, len(array)):
        #     list2.append({'index': j + 1, 'value': array[j]})
        list1.sort(key=lambda x: x['value'] + 0.0000001 * x['index'], reverse=True)
        #一般来说sort都是快速排序，是不稳定的排序。根据测试用例，他要求的是带有顺序的，越往后面，同一个值越大
        #也就是要求升序排列是稳定的，值 3 = 4 的时候，reverse降序排列才是4 3 1 2
        #但sort是不稳定的快速排序，所以在这里强行加了一个小数位，根据index的值控制大小，就不用自己实现一个
        #稳定的排序
        list2 = []
        for k in list1:
            list2.append(k['index'])
        dict[i + 1] = list2

    print("generatePerference return")
    print(dict)
    return dict


# completed
def dictatorship(preferenceProfile, agent):
    print("dictatorship")
    print(preferenceProfile)
    print(agent)
    print("END dictatorship")

    # 一个agent 决定一切，他的选择的第一个就是结果
    # 传进来的可能就不是排过序的，那就先
    # values = generatePerferences(preferenceProfile)
    # 格式是{1: [4, 2, 1, 3], 2: [3, 4, 1, 2], 3: [4, 3, 1, 2], 4: [1, 3, 4, 2], 5: [2, 3, 4, 1], 6: [2, 1, 3, 4]}
    # 需要注意value才是选票

    if agent in preferenceProfile.keys():
        return preferenceProfile[agent][0]
    # if agent in values.keys():
    #     return values[agent][0]  # 返回第一个

    return 0


def scoringRule(preferences, scoreVector, tieBreak):
    ## 看起来像是返回index，但不是很好确定，多测试几遍
    print("scoringRule")
    print(preferences)
    print(scoreVector)
    print(tieBreak)
    print("END scoringRule")

    # 找出最大
    vector_max = max(scoreVector)
    list_index = []
    for i in range(len(scoreVector)):
        # for val in dataset:
        if scoreVector[i] >= vector_max:
            list_index.append(i)

    if tieBreak == 'min':  # 找出最大的同时的最小index
        return min(list_index) + 1  # 他题目的index从1算起

    if tieBreak == 'max':
        return min(list_index) + 1  # 他题目的index从1算起

    if len(list_index) == 1:
        ## 如果没有tie，就用不着做过多计算
        return list_index[0] + 1  # 他题目的index从1算起

    # else 取index
    # list = []
    # list = list(set)
    # list.extend(set) # set 不可以 extend，因为set不能iterate
    rng = int(tieBreak)
    print("tieBreakFindValueByDict rng")
    print(rng)
    print(preferences[rng][0])
    return preferences[rng][0]


def plurality(preferences, tieBreak):
    print("plurality")
    print(preferences)
    print(tieBreak)
    print("END plurality")

    # 无论怎么样，要先calculate并汇总所有的投票
    # plurality意思是第一个出现得最多的 -- important
    # 传进来的可能就不是排过序的，那就先
    # values = generatePerferences(preferences)
    # 格式是{1: [4, 2, 1, 3], 2: [3, 4, 1, 2], 3: [4, 3, 1, 2], 4: [1, 3, 4, 2], 5: [2, 3, 4, 1], 6: [2, 1, 3, 4]}
    # 需要注意value(冒号右边）才是选票
    # 记录第一个出现的次数
    dict = {}
    for current_row in preferences.values():
        if current_row[0] not in dict.keys():  ##未经记录，设置为0
            dict[current_row[0]] = 0

        # 保证了选择存在dict，可以统计了
        dict[current_row[0]] += 1
    print("plurality dictionary")
    print(dict)
    print("END plurality dictionary")
    print(dict)

    return tieBreakFindValueByDict(preferences, dict, tieBreak)


def veto(preferences, tieBreak):
    print("veto")
    print(preferences)
    print(tieBreak)
    print("END veto")
    # # 无论怎么样，要先calculate并汇总所有的投票
    # # vento意思大概是 最后一个是0，那么除了最后一个，其他加1
    # # 传进来的可能就不是排过序的，那就先
    # values = generatePerferences(preferences)

    # 直接preferences可以计算
    values = preferences

    dict = {}
    for current_row in values.values():
        # 记录所有出现的次数，需要改用range
        for i in range(len(current_row)):
            if current_row[i] not in dict.keys():  ##未经记录，设置为0
                dict[current_row[i]] = 0
            # 保证了选择存在dict，可以统计了
            if i != len(current_row) - 1:  # 最后一个是0，那么除了最后一个，其他加1
                dict[current_row[i]] += 1

    return tieBreakFindValueByDict(preferences, dict, tieBreak)
    # return 0


def borda(preferences, tieBreak):
    print("borda")
    print(preferences)
    print(tieBreak)
    print("END borda")
    # 排序，最后一个0分，第一个m-1分，统计总分
    values = preferences
    dict = {}
    for current_row in values.values():
        leng = len(current_row)
        for i in range(0, leng):
            current = leng - i - 1  # 当前分数。当前的选择是pref[i]
            # 更新dictionary
            if current_row[i] not in dict.keys():  ##未经记录，设置为0
                dict[current_row[i]] = 0
            # 保证了选择存在dict，可以统计了
            dict[current_row[i]] = dict[current_row[i]] + current

    # 最终dict就是结果，但不能立刻返回
    return tieBreakFindValueByDict(preferences, dict, tieBreak)

    # return 0


def tieBreakFindValueByDict(preferences, dict, tieBreak):
    print("tieBreakFindValueByDict")
    print(dict)
    # 简单好懂的做法就是把最大的current_max挑出来
    # 把所有的选择都放进set
    dataset = []
    current_max = max(dict.values())
    for k in dict.keys():
        if current_max == dict[k]:
            dataset.append({"key": k, "value": dict[k]})
    print("tieBreakFindValueByDict dataset")
    print(dataset)

    if len(dataset) == 1:
        # 只剩下一个的时候，直接返回，不用下面的运算
        return dataset[0]['key']

    # 如果没有tie，就用不着做过多计算
    maxvalue = max(dict.values())
    list_to_remove = []
    for k2 in dict.keys():
        if dict[k2] < maxvalue:
            list_to_remove.append(k2)
            # 不能在dict循环的时候进行移除，这样改变了iterator的大小，铁定报错

    for item in list_to_remove:
        if item in dict.keys():
            dict.pop(item)

    # if len(dict.keys()) == 1:
    #     #只剩下一个的时候，直接返回，不用下面的运算
    #     list_to_remove.clear()
    #     list_to_remove.extend(dict.keys())
    #     #这里这么写，是非常个人风格的
    #     #list_to_remove是个列表，有学过数据结构应该知道，要么是数组要么是链表，但反正已经是分配过内存空间的
    #     #clear是清空列表原有的数据，但我并没有创建一个新的列表变量，所以实际上只分配了一次内存空间
    #     #后面再用同一个列表，把dict的key加进去，就省一次内存分配。但在python里面这些都看不到，或者做Python数据有关工作的人不会关心
    #     #不够内存反正加就是了
    #
    #     #dict.keys也能够取第一个返回，例如
    #     # for key3 in dict.keys():
    #     #     return key3
    #     #或者其他返回首个（唯一一个）元素的方法。我用list，只是个人习惯，或者我很喜欢用编辑器的.打开智能感应
    #     #很多写法是基于这个的
    #     ###### 一旦有人用了这一段
    #     ###### list_to_remove.clear()
    #     ###### list_to_remove.extend(dict.keys())
    #     ###### 十有八九这家伙抄你
    #     ###### 以上。
    #     print("tiebreak 1 return " + str(list_to_remove[0]) + "  ,,  " + dict.keys().__str__())
    #     return list_to_remove[0]

    #     current_max = max(current_max, dict[k])
    # for k in dict.keys():
    #     if dict[k] >= current_max:
    #         dataset.append(k)

    # print("tieBreakFindValueByDict dataset")
    # print(dataset)
    # # 然后set就是最大值的候选，多于一个则是同分
    # # 同分的时候，根据tieBreak选择
    # # 剩下的元素使用tieBreak
    if tieBreak == 'min':  # 找出最大的同时的最小index
        min_index = -1
        # current_min = 99999999
        for val in dataset:
            if min_index < 0:
                min_index = val['key']
            elif min_index > val['key']:
                min_index = val['key']
        print('min_index')
        print(min_index)
        return min_index

    if tieBreak == 'max':
        max_index = -1
        # current_max = 0
        for val in dataset:
            if max_index < 0:
                max_index = val['key']
            elif max_index < val['key']:
                max_index = val['key']
        print('max_index')
        print(max_index)
        return max_index

    # else 取index
    # list = []
    # list = list(set)
    # list.extend(set) # set 不可以 extend，因为set不能iterate
    rng = int(tieBreak)
    print("tieBreakFindValueByDict rng two " + str(rng))
    print(preferences[rng])
    print(dict)

    for prep in preferences[rng]:
        if prep in dict.keys():
            print("tieBreakFindValueByDict rng two return " + str(prep))
            return prep

    print("tieBreakFindValueByDict rng two return -1")
    return -1


def harmonic(preferences, tieBreak):
    print("harmonic")
    print(preferences)
    print(tieBreak)
    print("END harmonic")
    # 无论怎么样，要先calculate并汇总所有的投票
    # harmonic意思大概是 第一个就是1/1 最后一个1/m
    # 传进来的可能就不是排过序的，那就先
    values = generatePerferences(preferences)

    dict = {}
    for current_row in values.values():
        # 记录所有出现的次数，需要改用range
        for i in range(len(current_row)):
            if current_row[i] not in dict.keys():  ##未经记录，设置为0
                dict[current_row[i]] = 0.0
            # 保证了选择存在dict，可以统计了
            dict[current_row[i]] += (1.0 / float(i + 1))

    return tieBreakFindValueByDict(preferences, dict, tieBreak)
    # return 0


def STV(preferences, tieBreak):
    print("STV")
    print(preferences)
    print(tieBreak)
    print("END STV")
    # 无论怎么样，要先calculate并汇总所有的投票
    # STV意思好像是一票否决，最后一个留下的就是赢家
    # 格式是{1: [4, 2, 1, 3], 2: [3, 4, 1, 2], 3: [4, 3, 1, 2], 4: [1, 3, 4, 2], 5: [2, 3, 4, 1], 6: [2, 1, 3, 4]}
    # 需要注意value(冒号右边）才是选票

    # 每一次迭代，拿掉最后的那个
    dict = {}
    blocked = {}
    # 先统计
    # 先把所有元素都作为key加入dictionary
    for current_row in preferences.values():
        for i in range(len(current_row)):
            cell = current_row[i]
            if i == len(current_row) - 1:
                blocked[cell] = 1
                if cell in dict.keys():  ##未经记录，设置为0
                    dict.pop(cell)

                # 突然死亡制？
                if len(dict.keys()) == 1:
                    tmplist = list(dict.keys())
                    return tmplist[0]
            else:
                if cell not in blocked.keys() and cell not in dict.keys():  ##未经记录，设置为0
                    dict[cell] = 1
                # 保证了选择存在dict

    return tieBreakFindValueByDict(preferences, dict, tieBreak)
    # # 剩下的元素使用tieBreak
    # if tieBreak == 'min':
    #     return min(dataset)
    #
    # if tieBreak == 'max':
    #     return max(dataset)
    #
    # # else 取index
    # list = []
    # list.extend(set)
    # rng = int(tieBreak)
    # return list[rng]

    # return 0


def rangeVoting(values, tieBreak):
    print("rangeVoting")
    print(values)
    print(tieBreak)
    print("END rangeVoting")
    # 这个是最终需要实现的
    # rangeVoting没必要排序，先全部加上

    dict = {}  # 记录每个候选人的分数变化
    for prop in values:
        leng = len(prop)
        for i in range(0, leng):
            current = prop[i]  # 当前分数。当前的选择是 i
            # 更新dictionary
            if i not in dict.keys():  ##未经记录，设置为0
                dict[i] = 0
            # 保证了选择存在dict，可以统计了
            dict[i] = dict[i] + current

    # 最终dict就是结果，但不能立刻返回
    return tieBreakFindValueByDict(None, dict, tieBreak)
    # 然后根据tieBreak选出一个

    return 0
