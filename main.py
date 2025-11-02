import tkinter as tk
import random
import matplotlib.pyplot as plt
import time

# ------------------- SORTING FUNCTIONS -------------------
def bubble_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_i = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i]); i+=1
        else:
            result.append(right[j]); j+=1
    result+=left[i:]
    result+=right[j:]
    return result

def merge_sort(arr):
    if len(arr)<=1: return arr
    mid=len(arr)//2
    L=merge_sort(arr[:mid])
    R=merge_sort(arr[mid:])
    return merge(L,R)

def quick_sort(arr):
    if len(arr)<=1: return arr
    pivot = arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+mid+quick_sort(right)

# ------------------- GUI -------------------
root = tk.Tk()
root.title("Sorting Real Time Comparator")
root.geometry("650x450")

array = []

def generate_array():
    global array
    array = [random.randint(1,100) for _ in range(100)]
    lbl_arr_gen.config(text="Generated Array (first 40 shown): "+str(array[:40]))

def run_all_sorts():
    if not array:
        return

    times = {}
    sorted_output = None

    # measure real time
    def measure(name, func):
        arr_copy = array.copy()
        start = time.perf_counter()
        out = func(arr_copy)
        end = time.perf_counter()
        times[name] = (end-start)*1000
        return out

    sorted_output = measure("Bubble", bubble_sort)  # store one output to show
    measure("Selection", selection_sort)
    measure("Insertion", insertion_sort)
    measure("Merge", merge_sort)
    measure("Quick", quick_sort)

    lbl_arr_sorted.config(text="Sorted Array (first 40 shown): "+str(sorted_output[:40]))

    # bar chart
    plt.figure("Real Execution Time (ms)")
    plt.bar(times.keys(), times.values())
    plt.ylabel("Milliseconds (lower = faster)")
    plt.title("Real Time Complexity Comparison")
    plt.show()

btn1 = tk.Button(root,text="Generate Array",command=generate_array,bg="green",fg="white",width=30)
btn1.pack(pady=10)

btn2 = tk.Button(root,text="Sort Using All Algorithms & Compare Time",command=run_all_sorts,bg="blue",fg="white",width=40)
btn2.pack(pady=10)

lbl_arr_gen = tk.Label(root,text="Generated Array will display here",wraplength=600)
lbl_arr_gen.pack(pady=10)

lbl_arr_sorted = tk.Label(root,text="Sorted Array will display here",wraplength=600)
lbl_arr_sorted.pack(pady=10)

root.mainloop()
