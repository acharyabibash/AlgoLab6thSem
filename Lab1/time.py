from random import sample
from search import linear_search,binarySearchRecursive,binarySearchIterative
from time import time_ns
import matplotlib.pyplot as plt

# time_ns is for 

time_linear = []
time_binary = []
x_val =[]
time_lin= 0.00
time_bin = 0.00
# a = input('enter the beginning no of data')
# b= input ('enter the ending no of data')

def run():
    # data = sample(range(n+1),n)
    # print(data)
    # start_time = time_ns()
    for i in range(10000,100000+1,10000):
        input = i 
        data = sample(range(input+1),input)
        x_val.append(i)
        # print(x_val)
        # print(data)
        start_time_lin= time_ns()
        linear_search(data,data[-1]) # data[-1] is the last index of data so linear search is for worst case
        end_time_lin = time_ns()
        time_lin = end_time_lin - start_time_lin
        # print(time_lin)
        # print(start_time,end_time,time_taken)
        time_linear.append(time_lin)
        start_time_bin = time_ns()
        binarySearchRecursive(data,0,len(data)-1,data[-1])
        end_time_bin  = time_ns()
        time_bin = end_time_bin - start_time_bin
        time_binary.append(time_bin)


    # print(time_linear)
    plt.plot(x_val,time_linear,'red',label="linear search")
    plt.plot(x_val,time_binary,'blue',label="binary search")
    plt.suptitle("Worst Case Time Complexity")
    plt.xlabel("Number of data")
    plt.ylabel("Worst case search time in nanoseconds")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    run()

