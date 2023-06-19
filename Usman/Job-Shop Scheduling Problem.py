import queue


def costf(solution):
    days = 0
    totalDelay = 0
    for x in solution:
        days += jobs[x][0]
        print(str(x) + " completed on " + " day " + str(days))
        if days > jobs[x][1]:
            delay = days - jobs[x][1]
            totalDelay += delay
            print(str(x) + " delay = " + str(delay))
    return


def getFinal(seq):
    min = float('inf')
    final = 'Z'
    for x in seq:
        tmp = 24 - jobs[x][1]
        if tmp < min:
            min = tmp
            final = x
    return final


def JSSP(seq, beamSize=2):
    parent = getFinal(seq)
    seq.remove(parent)
    #print(seq)
    graph = {parent:seq}
    #for x in range(beamSize):
    delayList=[]
    for x in seq:
        delayList.append(24-jobs[parent][1]-jobs[x][1])
   # print(delayList)
    delayList.sort()
    print(delayList)
    topN=delayList[:2]
    print(topN)
    queue=[]
    #print(graph.values()
    return


if __name__ == "__main__":
    # jobs = ['A', 'B', 'C', 'D']
    # duration = [3, 5, 9, 7]
    # due = [5, 6, 16, 14]
    jobs = {'A': (3, 5), 'B': (5, 6), 'C': (9, 16), 'D': (7, 14)}
    totalDays = 0
    for x in jobs:
        totalDays += jobs[x][0]
    seq = ['A', 'B', 'C', 'D']
    #   costf(seq)
    JSSP(seq)
