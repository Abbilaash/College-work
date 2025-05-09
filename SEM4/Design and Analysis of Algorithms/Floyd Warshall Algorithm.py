def floywarshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]!=100000000 and dist[k][j]!=100000000:
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    print(dist)

INF = 100000000
dist = [
    [0,4,INF,5,INF],
    [INF,0,1,INF,6],
    [2,INF,0,3,INF],
    [INF,INF,1,0,2],
    [1,INF,INF,4,0]
    ]
floywarshall(dist)
