"""
Author: Venkata Sai Siva Prasad Mannem
For: R:V1 and R:V2 Sort Algorithms
Date: 03/06/2021
"""
###
## NOTE: Code under R:Version-1 and R:Version-2 name changed as R:V1 and R:V2
## Copy Rights taken on these R:V1 and R:V2 codes
###
import random
import time
#l = random.sample(range(200), 200)
#print(l)

l = [169, 104, 137, 148, 126, 149, 62, 7, 143, 57, 191, 194, 183, 69,
146, 22, 199, 3, 10, 163, 66, 170, 125, 109, 60, 187, 177, 25, 97, 42,
81, 132, 107, 172, 166, 94, 140, 134, 15, 180, 91, 160, 58, 105, 87,
152, 157, 117, 50, 82, 84, 72, 52, 164, 174, 67, 171, 77, 18, 44, 28,
192, 55, 48, 93, 33, 144, 130, 101, 8, 120, 43, 64, 176, 156, 100, 159,
129, 40, 153, 92, 89, 127, 106, 150, 37, 115, 158, 68, 165, 189, 119,
59, 128, 56, 154, 113, 41, 185, 167, 197, 45, 118, 141, 36, 1, 75, 78,
34, 175, 80, 31, 20, 102, 95, 173, 17, 13, 124, 162, 135, 19, 131, 98,
186, 2, 195, 21, 61, 188, 53, 110, 83, 190, 76, 46, 9, 145, 88, 168,
133, 138, 71, 196, 179, 27, 30, 198, 90, 193, 108, 184, 103, 123, 151,
122, 38, 142, 182, 29, 155, 23, 51, 70, 161, 147, 65, 39, 79, 96, 73,
116, 86, 178, 32, 35, 85, 181, 26, 54, 47, 24, 74, 4, 6, 99, 12, 0, 49,
63, 11, 139, 114, 5, 121, 136, 112, 111, 16, 14]
d = [169, 104, 137, 148, 126, 149, 62, 7, 143, 57, 191, 194, 183, 69,
146, 22, 199, 3, 10, 163, 66, 170, 125, 109, 60, 187, 177, 25, 97, 42,
81, 132, 107, 172, 166, 94, 140, 134, 15, 180, 91, 160, 58, 105, 87,
152, 157, 117, 50, 82, 84, 72, 52, 164, 174, 67, 171, 77, 18, 44, 28,
192, 55, 48, 93, 33, 144, 130, 101, 8, 120, 43, 64, 176, 156, 100, 159,
129, 40, 153, 92, 89, 127, 106, 150, 37, 115, 158, 68, 165, 189, 119,
59, 128, 56, 154, 113, 41, 185, 167, 197, 45, 118, 141, 36, 1, 75, 78,
34, 175, 80, 31, 20, 102, 95, 173, 17, 13, 124, 162, 135, 19, 131, 98,
186, 2, 195, 21, 61, 188, 53, 110, 83, 190, 76, 46, 9, 145, 88, 168,
133, 138, 71, 196, 179, 27, 30, 198, 90, 193, 108, 184, 103, 123, 151,
122, 38, 142, 182, 29, 155, 23, 51, 70, 161, 147, 65, 39, 79, 96, 73,
116, 86, 178, 32, 35, 85, 181, 26, 54, 47, 24, 74, 4, 6, 99, 12, 0, 49,
63, 11, 139, 114, 5, 121, 136, 112, 111, 16, 14]
f = [169, 104, 137, 148, 126, 149, 62, 7, 143, 57, 191, 194, 183, 69,
146, 22, 199, 3, 10, 163, 66, 170, 125, 109, 60, 187, 177, 25, 97, 42,
81, 132, 107, 172, 166, 94, 140, 134, 15, 180, 91, 160, 58, 105, 87,
152, 157, 117, 50, 82, 84, 72, 52, 164, 174, 67, 171, 77, 18, 44, 28,
192, 55, 48, 93, 33, 144, 130, 101, 8, 120, 43, 64, 176, 156, 100, 159,
129, 40, 153, 92, 89, 127, 106, 150, 37, 115, 158, 68, 165, 189, 119,
59, 128, 56, 154, 113, 41, 185, 167, 197, 45, 118, 141, 36, 1, 75, 78,
34, 175, 80, 31, 20, 102, 95, 173, 17, 13, 124, 162, 135, 19, 131, 98,
186, 2, 195, 21, 61, 188, 53, 110, 83, 190, 76, 46, 9, 145, 88, 168,
133, 138, 71, 196, 179, 27, 30, 198, 90, 193, 108, 184, 103, 123, 151,
122, 38, 142, 182, 29, 155, 23, 51, 70, 161, 147, 65, 39, 79, 96, 73,
116, 86, 178, 32, 35, 85, 181, 26, 54, 47, 24, 74, 4, 6, 99, 12, 0, 49,
63, 11, 139, 114, 5, 121, 136, 112, 111, 16, 14]
u = [169, 104, 137, 148, 126, 149, 62, 7, 143, 57, 191, 194, 183, 69,
146, 22, 199, 3, 10, 163, 66, 170, 125, 109, 60, 187, 177, 25, 97, 42,
81, 132, 107, 172, 166, 94, 140, 134, 15, 180, 91, 160, 58, 105, 87,
152, 157, 117, 50, 82, 84, 72, 52, 164, 174, 67, 171, 77, 18, 44, 28,
192, 55, 48, 93, 33, 144, 130, 101, 8, 120, 43, 64, 176, 156, 100, 159,
129, 40, 153, 92, 89, 127, 106, 150, 37, 115, 158, 68, 165, 189, 119,
59, 128, 56, 154, 113, 41, 185, 167, 197, 45, 118, 141, 36, 1, 75, 78,
34, 175, 80, 31, 20, 102, 95, 173, 17, 13, 124, 162, 135, 19, 131, 98,
186, 2, 195, 21, 61, 188, 53, 110, 83, 190, 76, 46, 9, 145, 88, 168,
133, 138, 71, 196, 179, 27, 30, 198, 90, 193, 108, 184, 103, 123, 151,
122, 38, 142, 182, 29, 155, 23, 51, 70, 161, 147, 65, 39, 79, 96, 73,
116, 86, 178, 32, 35, 85, 181, 26, 54, 47, 24, 74, 4, 6, 99, 12, 0, 49,
63, 11, 139, 114, 5, 121, 136, 112, 111, 16, 14]


'''
#### Cycle Sort
start = time.perf_counter()
tlc2 = 0
# Python program to implement cycle sort
# Loop through the array to find cycles to rotate.
for cycleStart in range(0, len(d) - 1):
    item = d[cycleStart]
    tlc2 += 1
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(d)):
            tlc2 += 1
            if d[i] < item:
                pos += 1
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
            continue
    # Otherwise, put the item there or right after any duplicates.
    while item == d[pos]:
            tlc2 += 1
            pos += 1
    d[pos], item = item, d[pos]
    # Rotate the rest of the cycle.
    while pos != cycleStart:
            tlc2 += 1
    # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(d)):
                tlc2 += 1
                if d[i] < item:
                    pos += 1
        # Put the item there or right after any duplicates.
            while item == d[pos]:
                tlc2 += 1
                pos += 1
            d[pos], item = item, d[pos]
end = time.perf_counter()
print(d)
print('cycle sort timegap: {0:.5f} start:{1} end:{2} loops: {3}'.format(end-start, start, end, tlc2))
'''

#### Online Geeks Version
start = time.perf_counter()
n = len(f)
tlc3 = 0
for i in range(n-1):
    tlc3 += 1
    for j in range(0, n-i-1):
        tlc3 += 1
        if f[j] > f[j+1]:
            f[j], f[j+1] = f[j+1], f[j]
end = time.perf_counter()
#print(f)
print('timegap: {0:.5f} start:{1} end:{2}'.format(end-start, start, end))

#### Online stackabuse Version
start = time.perf_counter()
n = len(u)
tlc4 = 0
for i in range(n-1):
    tlc4 += 1
    for j in range(n-1):
        tlc4 += 1
        if u[j] > u[j+1]:
            u[j], u[j+1] = u[j+1], u[j]
end = time.perf_counter()
#print(u)
print('timegap: {0:.5f} start:{1} end:{2}'.format(end-start, start, end))

'''
Copy Rights taken from here and ends at 'Copy Right Ended' comment
'''
#### R:Version-1
start = time.perf_counter()
c = 0
changed = False
tlc = 0
while c < len(l):
    tlc += 1
    if c+1 < len(l):
        if l[c] > l[c+1]:
            l[c], l[c+1] = l[c+1], l[c]
            changed = True
        if changed == True:
            t = c
            while 0 < t:
                tlc += 1
                if l[t] < l[t-1]:
                    l[t], l[t-1] = l[t-1], l[t]
                t -= 1
            changed = False
    c += 1
end = time.perf_counter()
#print(l)
print('timegap: {0:.5f} start:{1} end:{2}'.format(end-start, start, end))


#### R:Version-2
start = time.perf_counter()
tlc2 = 0
c = 0
while c < len(d):
    tlc2 += 1
    if c+1 < len(d):
        if d[c] > d[c+1]:
            d[c], d[c+1] = d[c+1], d[c]
        t = c
        while 0 < t:
            tlc2 += 1
            if d[t] < d[t-1]:
                d[t], d[t-1] = d[t-1], d[t]
            t -= 1
    c += 1
end = time.perf_counter()
#print(d)
print('timegap: {0:.5f} start:{1} end:{2}'.format(end-start, start, end))

print('number of loop: {0} {1} {2} {3}'.format(tlc, tlc2, tlc3, tlc4))
'''
Copy Right Ended
'''



'''
https://4movierulz.nl/waaw/?l=G32HAjQJV88f
'''
