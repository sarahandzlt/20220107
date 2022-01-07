def generatePerferences(values):
    dict = {}

    for i in range(0, len(values)):
        array = values[i]
        list2 = []
        for j in range(0, len(array)):
            list2.append({'index': j + 1, 'value': array[j]})
        list2.sort(key=lambda x: x['value'], reverse=True)

        sorted_list = [item['index'] for item in list2]

        dict[i + 1] = sorted_list

    return dict

# completed
def dictatorship(preferenceProfile, agent):
    print("dictatorship")
    print(preferenceProfile)
    print(agent)
    print("END dictatorship")

    # 一个agent 决定一切，他的选择的第一个就是结果
    # 传进来的可能就不是排过序的，那就先
    #values = generatePerferences(preferenceProfile)
    # 格式是{1: [4, 2, 1, 3], 2: [3, 4, 1, 2], 3: [4, 3, 1, 2], 4: [1, 3, 4, 2], 5: [2, 3, 4, 1], 6: [2, 1, 3, 4]}
    # 需要注意value才是选票

    if agent in preferenceProfile.keys():
        return preferenceProfile[agent][0]
    # if agent in values.keys():
    #     return values[agent][0]  # 返回第一个

    return 0


# TODO:
def scoringRule(preferences, scoreVector, tieBreak):
    print("scoringRule")
    print(preferences)
    print(scoreVector)
    print(tieBreak)
    print("END scoringRule")
    votesDict = {}
    values = generatePerferences(preferences)
    # 得出values
    return 0


def plurality(preferences, tieBreak):
    print("plurality")
    print(preferences)
    print(tieBreak)
    print("END plurality")

    # 无论怎么样，要先calculate并汇总所有的投票
    # plurality意思是第一个出现得最多的
    # 传进来的可能就不是排过序的，那就先
    values = generatePerferences(preferences)
    # 格式是{1: [4, 2, 1, 3], 2: [3, 4, 1, 2], 3: [4, 3, 1, 2], 4: [1, 3, 4, 2], 5: [2, 3, 4, 1], 6: [2, 1, 3, 4]}
    # 需要注意value(冒号右边）才是选票
    # 记录第一个出现的次数
    dict = {}
    for current_row in values.values():
        if current_row[0] not in dict.keys():  ##未经记录，设置为0
            dict[current_row[0]] = 0
        # 保证了选择存在dict，可以统计了
        dict[current_row[0]] += 1

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

    #直接preferences可以计算
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
    dict = {}  # 记录每个候选人的分数变化
    for pref in preferences:
        leng = len(pref)
        for i in range(0, leng):
            current = leng - i - 1  # 当前分数。当前的选择是pref[i]
            # 更新dictionary
            if pref[i] not in dict.keys():  ##未经记录，设置为0
                dict[pref[i]] = 0
            # 保证了选择存在dict，可以统计了
            dict[pref[i]] = dict[pref[i]] + current

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
            dataset.append({"key":k, "value":dict[k]})
    print("tieBreakFindValueByDict dataset")
    print(dataset)

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
    print("tieBreakFindValueByDict rng")
    print(rng)
    print(preferences[rng][0])
    return preferences[rng][0]


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
    #return 0


def STV(preferences, tieBreak):
    print("STV")
    print(preferences)
    print(tieBreak)
    print("END STV")
    # 无论怎么样，要先calculate并汇总所有的投票
    # STV意思好像是一票否决，最后一个留下的就是赢家
    # 传进来的可能就不是排过序的，那就先
    values = generatePerferences(preferences)
    # 格式是{1: [4, 2, 1, 3], 2: [3, 4, 1, 2], 3: [4, 3, 1, 2], 4: [1, 3, 4, 2], 5: [2, 3, 4, 1], 6: [2, 1, 3, 4]}
    # 需要注意value(冒号右边）才是选票

    key_list = []
    key_list.extend(values.keys())
    key_list.sort()
    # 每一次迭代，拿掉最后的那个
    dataset = set([])
    # 先把所有元素都加入set
    for prep in values.values():
        for p in prep:
            dataset.add(p)
    # 迭代所有，去掉最末尾
    for key in key_list:
        prep = values[key]
        if prep in dataset and len(dataset) > 1:
            dataset.remove(prep[-1])
        if len(dataset) == 1:
            return dataset.pop()

    # 剩下的元素使用tieBreak
    if tieBreak == 'min':
        return min(dataset)

    if tieBreak == 'max':
        return max(dataset)

    # else 取index
    list = []
    list.extend(set)
    rng = int(tieBreak)
    return list[rng]

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
            dict[i] = dict[i]+current

    # 最终dict就是结果，但不能立刻返回
    return tieBreakFindValueByDict(None, dict, tieBreak)
    # 然后根据tieBreak选出一个

    return 0
