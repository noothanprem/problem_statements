import pdb
import re


class Chess:

    chess_list=[]
    chess_list_copy=[]
    white_box_count=0
    black_box_count=0

    def create_board(self):

        black_pieces = ["brook1", "bknight1","bbishop1", "bqueen", "bking", "bbishop2", "bknight2", "brook2"]

        white_pieces = ["wrook1", "wknight1", "wbishop1", "wqueen", "wking", "wbishop2", "wknight2", "wrook2"]
        self.chess_list = [[x % 2 for x in range(8)] if x % 2 else [1 if x % 2 == 0 else 0 for x in range(8)] for x in
                      range(8)]
        self.chess_list_copy=self.chess_list
        for i in range(8):
            print(self.chess_list_copy[i])
        print(self.chess_list[0][0])
        # pdb.set_trace()
        print(len(self.chess_list[0]), "lengthhhhhhhh")
        for i in range(len(self.chess_list)):
            for j in range(len(self.chess_list[i])):

                if i == 0:
                    #print(black_pieces[j], "black piecess")
                    # print(chess_list[i][j], "0777")\
                    # print('dgfbj' ,i , j, len(black_pieces)
                    #if j == 7:
                        #break
                    self.chess_list[i][j] = black_pieces[j]

                elif (i == 1):

                    self.chess_list[i][j] = "bpawn" +  str(j + 1)

                elif (i == 6):

                    self.chess_list[i][j] = "wpawn" +  str(j + 1)

                elif (i == 7):

                    self.chess_list[i][j] = white_pieces[j]

                elif ((i + j) % 2 == 0):

                    self.chess_list[i][j] = 1


    def display_board(self):
        for row in self.chess_list:
            print(row)

    def pawn_move(self):
        pawn = input("Which pawn you want to move ? : ")
        pawnlist = self.chess_list[6]
        if pawn in pawnlist:
            count = 0
            while pawnlist[count] != pawn:
                count += 1
            pawnposition = count
            x = int(input("Enter the X position you want to move : "))
            y = int(input("Enter the Y position you want to move : "))
            if ((x == 4 and y == count) or (x == 5 and y == count)):
                if (x == 4 and y == count):
                    if (self.chess_list[4][count] == 1 or self.chess_list[4][count] == 0):
                        self.chess_list[4][count] = pawn
                        self.chess_list[6][count] = self.chess_list_copy[6][count]
                        self.display_board()

                    else:
                        print("Not Possible to kill any one in the inital move of pawn")
                        return


                elif (x == 5 and y == count):
                    if((self.chess_list[5][count] == '1') or (self.chess_list[5][count] == 0)):
                        #if(self.chess_list[5][count] == '0'):
                        self.chess_list[5][count]=pawn
                        self.chess_list[6][count]=self.chess_list_copy[6][count]
                        self.display_board()

            else:

                print("Invalid move try once again")
                return


        else:
            for i in range(len(self.chess_list)):
                for j in range(len(self.chess_list[i])):
                    if (self.chess_list[i][j] == pawn):
                        x = int(input("Enter the X position you want to move : "))
                        y = int(input("Enter the Y position you want to move : "))
                        if (x == i - 1 and (y == j - 1 or y == j + 1)):
                            regex_search = re.search("^w", str(self.chess_list[x][y]))
                            if ((self.chess_list[x][y] != 0 or self.chess_list[x][y] != 1) and (regex_search is None)):
                                self.chess_list[x][y] = pawn
                                self.chess_list[i][j] = self.chess_list_copy[i][j]
                                self.display_board()
                                return
                            else:
                                print("Pawns Cannot move Diagonally unless there is something in the square")
                                return
                    else:
                        if (i * j == 49):
                            print("Pawn not found")
                            return

    def rook_move(self):
        rook_name = input("Which rook you want to move ? : ")
        rooklist = ["wrook1", "wrook2"]
        if rook_name in rooklist:
            for i in range(len(self.chess_list)):
                for j in range(len(self.chess_list[i])):
                    if self.chess_list[i][j] == rook_name:
                        x = int(input("Enter the X value of the position you want to move : "))
                        y = int(input("Enter the Y value of the position you want to move : "))
                        if (x == i or y == j):
                            print(type(self.chess_list))
                            regex_search = re.search("^w", str(self.chess_list[x][y]))
                            print(regex_search,"regex searchhhh")

                            if (regex_search is None):
                                # if(self.chessboard[x][y] == 'X'):
                                self.chess_list[x][y] = rook_name
                                self.chess_list[i][j] = self.chess_list_copy[i][j]
                                self.display_board()
                                return
                            else:
                                print("Move invalid")
                                return
                        else:
                            print("Invalid move")
                            return
                    else:
                        if (i * j == 49):
                            print("rook name not found")
                            return
        else:
            print("Invalid wrook name")
            return

    def bishop_move(self):
        bishop_name = input("Which bishop you want to move : ")
        bishop_list = ["wbishop1", "wbishop2"]
        if bishop_name not in bishop_list:
            print("Invalid bishop name")
            return
        else:
            for i in range(len(self.chess_list)):
                for j in range(len(self.chess_list[i])):
                    #regex_check = re.search("^w", str(self.chess_list[i][j]))
                    #print(regex_check,"regex checkk")
                    #if regex_check is not None:
                        #print(self.chess_list[i][j],"chess list i j")
                        #if (self.chess_list[i][j] != bishop_name):
                            #print("Invalid moves")
                            #return
                    if (self.chess_list[i][j] == bishop_name):
                        x = int(input("Enter the X value of the position in which you want to insert : "))
                        y = int(input("Enter the Y value of the position in which you want to insert : "))
                        regex_search = re.search("^w", str(self.chess_list[x][y]))
                        if regex_search is not None:
                            print("Invalid move")
                            return
                        else:
                            if (abs((i - x)) == abs((j - y))):
                                self.chess_list[x][y] = bishop_name
                                self.chess_list[i][j] = self.chess_list_copy[i][j]
                                self.display_board()
                                return
                            else:
                                print("Invalid position")
                                return

    def queen_move(self):

        x=int(input("Enter the X value of the position you want to insert : "))
        y=int(input("Enter the y value of the position you want to insert : "))
        regex_search=re.search("^w",str(self.chess_list[x][y]))
        if regex_search is not None:
            print("Invalid move")
            return

        for i in range(len(self.chess_list)):
            for j in range(len(self.chess_list[i])):
                if(self.chess_list[i][j] == 'wqueen'):

                    if((abs(i-x) == abs(j-y)) or ((x == i) or (y == j))):
                        self.chess_list[x][y]=self.chess_list[i][j]
                        self.chess_list[i][j]=self.chess_list_copy[i][j]

                    else:
                        print("Invalid move")
                        return
                else:
                    if(i*j == 49):
                        print("Queen is not available")
                        return




if __name__ == '__main__':
    chessobject = Chess()
    chessobject.create_board()
    chessobject.display_board()
    #chessobject.pawn_move()
    #chessobject.rook_move()
    #chessobject.bishop_move()
    chessobject.queen_move()
