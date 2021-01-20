# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
_H, _W = input().rstrip().split()
H, W = int(_H), int(_W)

# make all the islands with padding one for each 
picture = [[] for i in range(H+2)]
for i in range(H+2):
    # top and bottom row should be filled with '.'
    if i == 0 or i == H+1:
        for j in range(W+2):
            picture[i].append('.')
    else:
        row = input()
        row = '.' + row + '.'
        for j in range(W+2):
            if j == 0 or j == W+1:
                picture[i].append('.')
            else:
                picture[i].append(row[j])
    

# calculating the area
ans_pic = [[0]*(W+2) for i in range(H+2)]

def seek_neighbor(i, j, is_from):
    
    boundries = 0
    if picture[i][j] == '.':
        return [0, 1]
        
    if ans_pic[i][j] != 0:
        return [0, 0]
        
    ans_pic[i][j] = 1
    
    # below, it must have '#' in (i,j)
    count = 1
    if is_from == 'north':
        _count, _boundries = seek_neighbor(i+1,j, 'north')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i,j+1, 'west')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i,j-1, 'east')
        count += _count
        boundries += _boundries
        
    elif is_from == 'south':
        _count, _boundries = seek_neighbor(i-1,j, 'south')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i,j+1, 'west')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i,j-1, 'east')
        count += _count
        boundries += _boundries
        
    elif is_from == 'west':
        _count, _boundries = seek_neighbor(i+1,j, 'north')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i-1,j, 'south')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i,j+1, 'west')
        count += _count
        boundries += _boundries
        
    elif is_from == 'east':
        _count, _boundries = seek_neighbor(i+1,j, 'north')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i-1,j, 'south')
        count += _count
        boundries += _boundries
        
        _count, _boundries = seek_neighbor(i,j-1, 'east')
        count += _count
        boundries += _boundries

    return [count, boundries];

#def count_boundies():
    
    

ans = []
for i in range(H+2):
    for j in range(W+2):
        if picture[i][j] == '#' and ans_pic[i][j] == 0:
            count, boundries = seek_neighbor(i, j, 'west')
            ans.append([count, boundries+1]) 

ans.sort(reverse=True)

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])

