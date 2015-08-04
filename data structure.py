
python数据结构初识
1、数据结构有元组、字典、队列、栈、树等
2、python内置数据结构：列表、元组、字典等
3、python扩展数据结构：栈、队列等

【列表】存储方式一：可取出、更换
["apple","orange","pear"]

【元组】存储方式二：不可取出、更换
("apple","orange","pear")

【字典】存储方式三：每个柜子中有名称，可取出、更换  {"键":"值"}
{"Sam":"apple","Bill":"orange","Gate"："pear"}


栈
#栈的实现
class Stack():
    def __init__(st,size):
        st.stack = [];
        st.size = size;
        st.top = -1;
        
    def push(st,content):
        if st.Full():
            print "Stack is Full!"
        else:
            st.stack.append(content)
            st.top = st.top + 1
    def out(st):
        if st.Empty():
            print "Stack is Empty"
        else:
            st.top = st.top-1
    
    def Full(st):
        if st.top ==st.size:
            return True
        else:
            return False
            
    def Empty(st):
        if st.top == -1:
            return True
        else:
            return False
-----------------------------------------------------------
>>q=Stack(7)        # 创建一个Stack类的变量，大小为7
>>q.Empty()       #  检测栈是否为空
>>q.push（"hello"）    #  hello入栈
>>q.push("Sunday")     #  Sunday入栈
>>q.out()    # 出栈




#队列

class Queue():
    
    def __init__(qu,size):
        qu.queue = [];
        qu.size = size;
        qu.head = -1;
        qu.tail = -1;
    
    def Empty(qu):
        if qu.head == qu.tail:
            return True
        else:
            return False
    
    def Full(qu):
        if qu.tail - qu.head +1 == qu.size:
            return True
        else:
            return False
    
    def enQueue(qu,content):
        if qu.Full:
            print "Queue is Full!"
        else:
            qu.queue.append(content)
            qu.tail = qu.tail + 1
    
    def outQueue(qu):
        if qu.Empty():
            print "Queue is Empty!"
        else:
            qu.head = qu.head + 1
-----------------------------------------------------


树

class TRee():
    def __init__(self,leftjd=0,rightjd=0,data=0):
        self.leftjd = leftjd;
        self.rightjd = rightjd;
        self.data = data;
    
class Btree():
    def __init__(self,base=0):
        self.base = base
    
    def empty(self):
        if self.base is 0:
            return True
        else:
            return False
    
    def qout(self,jd):
        '''前序遍历，NLR，根左右'''
        if jd == 0:
            return
        print jd.data
        self.qout(jd.leftjd)
        self.qout(jd.rightjd)
        
    def mout(self,jd):
        '''中序遍历，LNR，左根右'''
        if jd == 0:
            return
        self.mout(jd.leftjd)
        print jd.data
        self.mout(jd.rightjd)
        
    def hout(self,jd):
        '''后序遍历，LRN，左右根'''
        if jd == 0:
            reutrn
        self.hout(jd.leftjd)
        self.hout(jd.rightjd)
        print jd.data
------------------------------------------------------------------------
>>jd1 = TRee(data = 8)      #创建节点1
>>jd2 = TRee(data = 9)      #创建节点2
>>base = TRee(jd1,jd2,7)     #创建根节点
>>x=Btree(base)      #输入根节点为base的一棵树
>>x.qout(x.base)     #前序遍历
>>x.mout(x.base)     #中序遍历
>>x.hout(x.base)     #后序遍历




链表

class jd():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist():
    def __init__(self,jd2):
        self.head = jd2        #head\tail是节点
        self.head.next = None
        self.tail = self.head
    
    def add(self,jd2):
        self.tail.next = jd2
        self.tail = self.tail.next
        
    def view(self):
        jd2 = self.head
        linkstr = ""
        while jd2 is not None:
            if jd2.next is not None:
                linkstr = linkstr + str(jd2.data) + "-->"
            else:
                linkstr = linkstr + str(jd2.data)
            jd2 = jd2.next
        print linkstr

---------------------------------------------------------------------
>>jd1 = jd(7)     #创建节点1
>>jd2 = jd("hello")     #创建节点2
>>jd3 = jd(2015)     #创建节点3
>>x = Linklist(jd1)     #声明一个链表Linklist对象 x，传入节点1作首节点
>>x.add(jd2)     #将节点2、3链接起来
>>x.add(jd3)     #将节点2、3链接起来
>>x.view()     #遍历节点



