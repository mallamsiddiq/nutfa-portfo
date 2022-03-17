import bisect
import time

# starting time
start = time.time()

cards = ['Jack', 8, 2, 6, 5, 3,'Jack','Jack','King','King','Queen','Queen','Jack']
# cards.sort()

def helloWorld(arr):
    int_arr=[]
    obj_arr=[]
    kings_count=arr.count('King')
    kings_arr=[]
    
    for i in arr:
        if type(i)==int:
            bisect.insort(int_arr, i)
            # int_arr.append(i)
        elif i!='King':
            # obj_arr.append(i)
            bisect.insort(obj_arr, i)
    # int_arr.sort()
    # obj_arr.sort()


    reformed_arr=int_arr+obj_arr+['King']*kings_count


    print(reformed_arr)
    # print (arr)

# helloWorld(cards)

print(time.time()-kkkkkkkkkkkkkstart)

class MyArray(list):
    """docstring for MyArray"""
    def __init__(self, arr):
        # super(MyArray, self).__init__()
        self.arr = arr
        self.int_arr=[]
        self.obj_arr=[]
    def sort(self):
        try:
            self.sort()
        except Exception as e:
            if self==[]:
                pass
            else:
                self.int_arr= self.filter(lambda x: type(x)==int, sequence)
                self.obj_arr=self-self.int_arr
                self.obj_arr.remove('King'*)
        pass

# Your Previous  code is preserved below:
# var cards = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen']
# Requried Output = [2,3,5,6,8,'Jack','Queen','King']
# Q: Sort the array as per the rules of card game using generic method.
# Choose language of your choice.

