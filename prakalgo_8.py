# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @\n')
def karakter_ganjil(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            result += input_string[i]
    return result

input_user = input("Masukkan sebuah kata :  ")

hasil = karakter_ganjil(input_user)

print("Karakter index ganjil : ", hasil)

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @\n')
def hitung_jumlah_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

start = int(input("Masukkan angka pertama : "))
end = int(input("Masukkan angka kedua : "))

hasil = hitung_jumlah_range(start, end)
print(f"Jumlah range adalah {hasil}")