def maxMeetings(N,S,F):
    data=[]
    for i in range(N):
        data.append((F[i],S[i]))
    data= sorted(data)
    count=0
    prev_end=-1
    for i in range(N):
        if(data[i][1]>prev_end):
            count+=1
            prev_end=data[i][0]
    return count
print(maxMeetings(8,[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924], [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252 ]))
