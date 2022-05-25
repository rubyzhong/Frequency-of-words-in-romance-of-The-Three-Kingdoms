import jieba
import os
os.chdir(r'D:\python\python文件操作')
article = open('三国演义.txt', 'r', encoding='utf-8').read()
words = jieba.lcut(article)

exincludes = ['将军', '却说', '二人', '不可', '荆州', '如此', '不能',
            '商议', '如何', '主公', '军士', '左右', '军马', '引兵',
            '次日', '大喜', '天下', '于是', '东吴', '今日', '不敢',
            '魏兵', '人马', '不知', '汉中', '陛下', '一人', '众将',
            '只见', '蜀兵', '大叫', '上马', '此人', '后人', '城中',
            '背后', '一面', '先主', '太守', '大军', '何不', '然后',
            '忽报', '先生', '夫人', '不如', '先锋', "何故", '江东',
            '原来', '令人', '天子', '赶来', '徐州', '正是', '忽然',
            '下马', '因此', '大败', '未知', '百姓', '成都', '大事',
            '一军', '之后', '起兵', '喊声', '不见', '接应', '引军',
            '进兵', '引军', '军中', '大怒', '大惊', '可以', '谋反',
            '心中', '以为', '军民', '不得', '休走', '帐中', '可得']
nums = {}
for word in words:
    if len(word) == 1 or word in exincludes:
        continue
    elif word in ['丞相','曹孟德','孟德']:
        nums['曹操'] = nums.get('曹操', 0) + 1
    elif word in ['孔明曰', '诸葛亮','卧龙','伏龙','武乡侯','忠武侯','蜀相']:
        nums['孔明'] = nums.get('孔明', 0) + 1
    elif word in ['玄德曰', '玄德' , '刘豫州','汉中王','汉昭烈帝','平原相','汉室宗亲','中山靖王之后','刘皇叔']:
        nums['刘备'] = nums.get('刘备', 0) + 1
    elif word in ['关公', '云长','寿亭侯','关云长']:
        nums['关羽'] = nums.get('关羽', 0) + 1
    elif word in ['都督','周郎','公瑾']:
        nums['周瑜'] = nums.get('周瑜', 0) + 1
    elif word in ['飞将','吕温侯','奉先','吕奉先']:
        nums['吕布'] = nums.get('吕布', 0) + 1
    elif word in ['常胜将军','子龙','赵子龙']:
        nums['赵云'] = nums.get('赵云',0)+1
    else:
        nums[word] = nums.get(word, 0) + 1
numslist = list(nums.items())
numslist.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = numslist[i]
    print("{} {}".format(word, count))
