class HeatMap:

    def __init__(self):
        self.heatmap = [[0 for _ in range(10)] for _ in range(10)]

    def updateHeatmap(self, occupied):
        for x,y in occupied:
            self.heatmap[x][y] += 1
        