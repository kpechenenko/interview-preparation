class Solution:  
    def _recursivelyFill(self, sr: int, sc: int, replaceable_color: int, new_color: int) -> None:
        if (sr >= 0 and sr < self.n 
            and sc >= 0 and sc < self.m 
            and not self.seen[sr][sc]):
            self.seen[sr][sc] = True
            if (self.img[sr][sc] == replaceable_color):
                self.img[sr][sc] = new_color
                self._recursivelyFill(sr - 1, sc, replaceable_color, new_color)
                self._recursivelyFill(sr + 1, sc, replaceable_color, new_color)
                self._recursivelyFill(sr, sc - 1, replaceable_color, new_color)
                self._recursivelyFill(sr, sc + 1, replaceable_color, new_color)

    
    def floodFill(self, img: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        self.img = img
        self.n = len(self.img)
        self.m = len(self.img[0])
        self.seen = [[False for _ in range(self.m)] for _ in range(self.n)]
        self._recursivelyFill(sr, sc, img[sr][sc], new_color)
        return self.img
            
