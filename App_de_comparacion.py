import random
import time
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Funciones de ordenamiento

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]  
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left_side = [elem for elem in arr[1:] if elem <= pivot]
        right_side = [elem for elem in arr[1:] if elem > pivot]
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # intercambiar
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        i = 0
        swapped = False
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n-1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1

        swapped = False
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        start += 1

# Generar una lista aleatoria de números
arr = [random.randint(0, 5) for _ in range(1000)]

# Comparar el tiempo de ejecución de cada algoritmo
start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(arr.copy())
selection_sort_time = time.time() - start_time

start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

start_time = time.time()
shell_sort(arr.copy())
shell_sort_time = time.time() - start_time

start_time = time.time()
merge_sort(arr.copy())
merge_sort_time = time.time() - start_time

start_time = time.time()
quick_sort(arr.copy())
quick_sort_time = time.time() - start_time

start_time = time.time()
heap_sort(arr.copy())
heap_sort_time = time.time() - start_time

start_time = time.time()
comb_sort(arr.copy())
comb_sort_time = time.time() - start_time

start_time = time.time()
cocktail_sort(arr.copy())
cocktail_sort_time = time.time() - start_time

# Graficar los tiempos de ejecución
plt.ion()  # activar modo interactivo
fig, ax = plt.subplots()
n = [i for i in range(30, 10001, 30)]
bubble_times = []
selection_times = []
insertion_times = []
shell_sort_time = []
merge_sort_time = []
quick_sort_time = []
heap_sort_time = []
comb_sort_time = []
cocktail_sort_time = []
for i in n:
    arr = [random.randint(0, 5) for _ in range(i)]

    start_time = time.time()
    bubble_sort(arr.copy())
    bubble_times.append(time.time() - start_time)

    start_time = time.time()
    selection_sort(arr.copy())
    selection_times.append(time.time() - start_time)

    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_times.append(time.time() - start_time)

    start_time = time.time()
    shell_sort(arr.copy())
    shell_sort_time.append(time.time() - start_time)

    start_time = time.time()
    merge_sort(arr.copy())
    merge_sort_time.append(time.time() - start_time)

    start_time = time.time()
    quick_sort(arr.copy())
    quick_sort_time.append(time.time() - start_time)

    start_time = time.time()
    heap_sort(arr.copy())
    heap_sort_time.append(time.time() - start_time)

    start_time = time.time()
    comb_sort(arr.copy())
    comb_sort_time.append(time.time() - start_time)

    start_time = time.time()
    cocktail_sort(arr.copy())
    cocktail_sort_time.append(time.time() - start_time)

    ax.clear()  # borrar gráfica anterior
    ax.plot(n[:len(bubble_times)], bubble_times, label='Bubble Sort')
    ax.plot(n[:len(selection_times)], selection_times, label='Selection Sort')
    ax.plot(n[:len(insertion_times)], insertion_times, label='Insertion Sort')
    ax.plot(n[:len(shell_sort_time)], shell_sort_time, label='Shell Sort')
    ax.plot(n[:len(merge_sort_time)], merge_sort_time, label='Merge Sort')
    ax.plot(n[:len(quick_sort_time)], quick_sort_time, label='Quick Sort')  
    ax.plot(n[:len(heap_sort_time)], heap_sort_time, label='Heap Sort')
    ax.plot(n[:len(comb_sort_time)], comb_sort_time, label='Comb Sort')
    ax.plot(n[:len(cocktail_sort_time)], cocktail_sort_time, label='Cocktail Sort')
    ax.legend(loc='upper left')
    ax.set_xlabel('Tamaño del arreglo')
    ax.set_ylabel('Tiempo de ejecución (segundos)')
    plt.pause(0.1)  # pausa para actualizar la gráfica
    #Echo por
    #Javier Armando Cruz Jahuira
    #David Huichi Calderon
    #Flavio Zapana Ticona