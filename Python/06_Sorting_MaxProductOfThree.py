# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # 絶対値の昇順でプラス，マイナス，ゼロに分ける
    arr = sorted(A, key=abs) 
    plusArr = []
    minusArr = []
    zeroArr = []
    for a in arr:
        if a > 0: plusArr.append(a)
        elif a < 0: minusArr.append(a)
        else: zeroArr.append(a)
    # end of for

    # プラス，マイナスの上位3個と下位3個を切り出す(それ以外は必要ない)
    # 同じ範囲を2回切り出さないように注意
    tmpArr = []
    if 0 < len(plusArr) <= 6: tmpArr += plusArr
    else:
        tmpArr += plusArr[:3]
        tmpArr += plusArr[-3:]
    
    if 0 < len(minusArr) <= 6: tmpArr += minusArr
    else:
        tmpArr += minusArr[:3]
        tmpArr += minusArr[-3:]
    
    if len(zeroArr) > 0: tmpArr += zeroArr[:3]
        
        
    # tmpArrで全探索(最大で7C3なので余裕)
    ans = -float('inf')
    tn = len(tmpArr)
    for i in range(tn - 2):
        for j in range(i + 1, tn - 1):
            for k in range(j + 1, tn):
                tmp = tmpArr[i] * tmpArr[j] * tmpArr[k]
                ans = max(ans, tmp)
    # end of for 
    
    #print(tmpArr)
    return ans
# end of func