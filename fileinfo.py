#管理信息系统git作业
#18377324 王鑫


#引用必要的库
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import tkinter.messagebox as ms
import webbrowser as wb

#输入从网上找到的停用词表
stoplist=['a', "a's", 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'adopted', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'apparently', 'appear', 'appreciate', 'appropriate', 'approximately', 'are', 'area', 'areas', 'aren', "aren't", 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asked', 'asking', 'asks', 'associated', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'began', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'beings', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'big', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', "c'mon", "c's", 'ca', 'came', 'can', "can't", 'cannot', 'cant', 'case', 'cases', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clear', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'couldnt', 'course', 'currently', 'd', 'date', 'definitely', 'describe', 'described', 'despite', 'did', "didn't", 'differ', 'different', 'differently', 'discuss', 'do', 'does', "doesn't", 'doing', "don't", 'done', 'down', 'downed', 'downing', 'downs', 'downwards', 'due', 'during', 'e', 'each', 'early', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ended', 'ending', 'ends', 'enough', 'entirely', 'especially', 'et', 'et-al', 'etc', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'ff', 'fifth', 'find', 'finds', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthermore', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'going', 'gone', 'good', 'goods', 'got', 'gotten', 'great', 'greater', 'greatest', 'greetings', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hed', 'hello', 'help', 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'hither', 'home', 'hopefully', 'how', 'howbeit', 'however', 'hundred', 'i', "i'd", "i'll", "i'm", "i've", 'id', 'ie', 'if', 'ignored', 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inasmuch', 'inc', 'include', 'indeed', 'index', 'indicate', 'indicated', 'indicates', 'information', 'inner', 'insofar', 'instead', 'interest', 'interested', 'interesting', 'interests', 'into', 'invention', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'itd', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'keys', 'kg', 'kind', 'km', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'lately', 'later', 'latest', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'lets', 'like', 'liked', 'likely', 'line', 'little', 'long', 'longer', 'longest', 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'making', 'man', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'member', 'members', 'men', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', "n't", 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needed', 'needing', 'needs', 'neither', 'never', 'nevertheless', 'new', 'newer', 'newest', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'novel', 'now', 'nowhere', 'number', 'numbers', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'older', 'oldest', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'open', 'opened', 'opening', 'opens', 'or', 'ord', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'parted', 'particular', 'particularly', 'parting', 'parts', 'past', 'per', 'perhaps', 'place', 'placed', 'places', 'please', 'plus', 'point', 'pointed', 'pointing', 'points', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'presented', 'presenting', 'presents', 'presumably', 'previously', 'primarily', 'probably', 'problem', 'problems', 'promptly', 'proud', 'provides', 'put', 'puts', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'reasonably', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'room', 'rooms', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'second', 'secondly', 'seconds', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'sees', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', "she'll", 'shed', 'shes', 'should', "shouldn't", 'show', 'showed', 'showing', 'shown', 'showns', 'shows', 'side', 'sides', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'state', 'states', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 't', "t's", 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", "that's", "that've", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there'll", "there's", "there've", 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'thereof', 'therere', 'theres', 'thereto', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'theyd', 'theyre', 'thing', 'things', 'think', 'thinks', 'third', 'this', 'thorough', 'thoroughly', 'those', 'thou', 'though', 'thoughh', 'thought', 'thoughts', 'thousand', 'three', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'today', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'turn', 'turned', 'turning', 'turns', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', "wasn't", 'way', 'ways', 'we', "we'd", "we'll", "we're", "we've", 'wed', 'welcome', 'well', 'wells', 'went', 'were', "weren't", 'what', "what'll", "what's", 'whatever', 'whats', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', "who'll", "who's", 'whod', 'whoever', 'whole', 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'words', 'work', 'worked', 'working', 'works', 'world', 'would', "wouldn't", 'www', 'x', 'y', 'year', 'years', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'youd', 'young', 'younger', 'youngest', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'z', 'zero', 'zt', 'zz']

#打开文件并进行预处理
#运行时需要修改文件位置
text=open(r'C:\Users\13052\Desktop\test.txt','r')
text=text.read()
origntext=text
text=text.lower()
#去除掉标点符号
text=text.replace(',',' ')
text=text.replace('.',' ')
text=text.replace('?',' ')
text=text.replace(':',' ')
text=text.replace(';',' ')
text=text.replace('(',' ')
text=text.replace(')',' ')
text=text.replace('\"',' ')
text=text.replace('\'',' ')
#化为包含单词的列表
stext=text.split()

#定义统计单词数函数
def total(stext):
    lens=len(stext)
    print(lens)
    ms.showinfo(title='全文总词数',message='总词数为:'+str(lens))

#定义单词使用次数函数
def times(stext):
    word=[]
    tims=[]
    for i in stext:
        if i in word:
            nub=word.index(i)
            tims[nub]=tims[nub]+1
        else:
            word.append(i)
            tims.append(1)
    for i in range(len(word)):
        print(word[i],tims[i])


#定义关键词输出及画图函数
def important(stext):
    impword=[]
    imptims=[]
    for i in stext:
        if i not in stoplist:
            if i not in impword:
                impword.append(i)
                imptims.append(1)
            else:
                impnub=impword.index(i)
                imptims[impnub]+=1
    at=1
    maxword=[]
    maxtims=[]
    while at<=6:
        maxt=max(imptims)
        maxtims.append(maxt)
        maxw=imptims.index(maxt)
        maxword.append(impword[maxw])
        impword.remove(impword[maxw])
        imptims.remove(maxt)
        at=at+1
    maxtims=np.array(maxtims)
    maxword=np.array(maxword)
    width=0.35
    fig,ax=plt.subplots()
    rects1=ax.bar(maxword,maxtims,width)
    plt.show()
    
#创建超链接所用函数
def pm():
    wb.open('http://mail.163.com/')
def bd():
    wb.open('http://www.baidu.com/')


b1.grid_configure(column=1,row=1,columnspan=1,rowspan=1)
b2.grid_configure(column=2,row=1,columnspan=1,rowspan=1)
b3.grid_configure(column=3,row=1,columnspan=1,rowspan=1)
t1=Text(top,bg='yellow',fg='green')

t1=Text(top,bg='yellow',fg='green')
t1.insert(INSERT,origntext)
t1.grid_configure(column=1,row=2,columnspan=3,rowspan=1)
b4=Button(top,width=25,text='网易邮箱',command=lambda:pm(),bg='yellow',fg='green')