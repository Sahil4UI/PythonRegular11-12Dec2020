import random

combinations = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]

    ]

positions = [i for i in range(1,10)]

def gameBoard():
    print(
        f"""
                {positions[0]}  |  {positions[1]}  |  {positions[2]}
                ----------------
                {positions[3]}  |  {positions[4]}  |  {positions[5]}
                ----------------
                {positions[6]}  |  {positions[7]}  |  {positions[8]}
                
        """
        )
gameBoard()
