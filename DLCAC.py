# Make sure your interpreter is set to the python 3.8.5 32-bit, global option
# To Do
# premium, benefit, loss, P(loss) calculation ):
# I: a1x:n
# II: tpxy, tqxy, u|tqxy, tq1xy, tq2xy, tpxybar, tqxybar, u|tqxybar, abarxy, abarxy:n, Abar
# rename/organize
import pandas as pd
# import scipy
import tkinter as tk
from tkinter import StringVar, IntVar

# placements of outputs and variable names in the window.
out_y = 180
out_x1 = 50
out_x2 = 280
out_x3 = 510
out_x4 = 740
s = 40 # space between variable and output.
r = 10 # Rounding Accuracy.

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dave's Life Contingent Actuarial Calculator")
        self.width = 1200 # width for the Tk root
        self.height = 600 # height for the Tk root
        # get screen width and height
        self.screen_width = self.winfo_screenwidth() # width of the screen
        self.screen_height = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/1.8) 
        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.e5 = StringVar()
        self.e6 = StringVar()

        # Manually input Standard Ultimate/Select Table lx and l[x]
        self.df = pd.DataFrame(data={ \
                                "lx": ["N/A", "N/A", 100000, 99975, 99950, 99924, 99898, 99871, 99844, 
                                       99816, 99787, 99758, 99727, 99696, 99663, 99629, 99594, 99557, 
                                       99518, 99477, 99433, 99387, 99338, 99286, 99230, 99169, 99104, 
                                       99034, 98958, 98874, 98784, 98685, 98576, 98457, 98326, 98182, 
                                       98022, 97846, 97651, 97435, 97196, 96930, 96634, 96306, 95941, 
                                       95534, 95083, 94580, 94020, 93398, 92706, 91937, 91082, 90134, 
                                       89082, 87917, 86628, 85203, 83633, 81904, 80006, 77927, 75657, 
                                       73186, 70507, 67615, 64507, 61185, 57657, 53935, 50039, 45996, 
                                       41841, 37619, 33380, 29184, 25094, 21178, 17502, 14126, 11103, 
                                       8470, 6248, 4439, 3023, 1962, 1208, 700, 379, 190, 
                                       88, 37, 14, 5, 1, 0, 0, 0, 0, 
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                       0, 0, 0, 0, 0
], 
                                "l[x]": [100044, 100020, 99995, 99970, 99945, 99919, 99893, 99866, 99838, 
                                         99810, 99781, 99752, 99721, 99689, 99656, 99622, 99586, 99549, 
                                         99510, 99468, 99424, 99378, 99328, 99275, 99218, 99156, 99090, 
                                         99019, 98941, 98856, 98764, 98663, 98553, 98431, 98297, 98150, 
                                         97987, 97807, 97608, 97387, 97142, 96870, 96568, 96232, 95859, 
                                         95444, 94981, 94467, 93895, 93259, 92551, 91765, 90891, 89922, 
                                         88847, 87656, 86340, 84885, 83283, 81519, 79584, 77466, 75154, 
                                         72640, 69916, 66978, 63825, 60459, 56889, 53128, 49198, 45129, 
                                         40956, 36725, 32491, 28311, 24253, 20382, 16764, 13458, 10515, 
                                         7967, 5833, 4109, 2771, 1780, 1082, 619, 330, 163, 
                                         74, 30, 11, 4, 1, 0, 0, 0, 0, 
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                         0, 0, 0, 0, 0]
}) \

        # Output Labels
        tk.Label(self, text = "Survival Probabilities\n 17 < t + x + u < 130").place(x = 0, y = 0)
        tk.Label(self, text = "tpx = ").place(x = out_x1-s, y = (out_y+24*0))
        tk.Label(self, text = "tqx = ").place(x = out_x1-s, y = (out_y+24*1))
        tk.Label(self, text = "u|tqx = ").place(x = out_x1-s, y = (out_y+24*2))
        tk.Label(self, text = "ex = ").place(x = out_x1-s, y = (out_y+24*3))
        tk.Label(self, text = "2ex = ").place(x = out_x1-s, y = (out_y+24*4))
        tk.Label(self, text = "V(Tx) = ").place(x = out_x1-s, y = (out_y+24*5))
        tk.Label(self, text = "ex:n = ").place(x = out_x1-s, y = (out_y+24*6))
        tk.Label(self, text = "2ex:n = ").place(x = out_x1-s, y = (out_y+24*7))
        tk.Label(self, text = "V(min(Tx, n)) = ").place(x = out_x1-s, y = (out_y+24*8))
        tk.Label(self, text = "Ax = ").place(x = out_x1-s, y = (out_y+24*9))
        tk.Label(self, text = "2Ax = ").place(x = out_x1-s, y = (out_y+24*10))
        tk.Label(self, text = "V(v^Tx) = ").place(x = out_x1-s, y = (out_y+24*11))
        tk.Label(self, text = "Ax:n = ").place(x = out_x1-s, y = (out_y+24*12))
        tk.Label(self, text = "2Ax:n = ").place(x = out_x1-s, y = (out_y+24*13))
        tk.Label(self, text = "V(min(v^Tx, n)) = ").place(x = out_x1-s, y = (out_y+24*14))
        tk.Label(self, text = "u|Ax = ").place(x = out_x1-s, y = (out_y+24*15))
        tk.Label(self, text = "u|Ax:n = ").place(x = out_x1-s, y = (out_y+24*16))

        tk.Label(self, text = "nEx = ").place(x = out_x2-s, y = (out_y+24*0))
        tk.Label(self, text = "2nEx = ").place(x = out_x2-s, y = (out_y+24*1))
        tk.Label(self, text = "V(min(v^Tx, n)*I(Tx>n)) = ").place(x = out_x2-s, y = (out_y+24*2))
        tk.Label(self, text = "A1x:n = ").place(x = out_x2-s, y = (out_y+24*3))
        tk.Label(self, text = "2A1x:n = ").place(x = out_x2-s, y = (out_y+24*4))
        tk.Label(self, text = "V(min(v^Tx, n)*I(Tx<n)) = ").place(x = out_x2-s, y = (out_y+24*5))
        tk.Label(self, text = "ax = ").place(x = out_x2-s, y = (out_y+24*6))
        tk.Label(self, text = "ax:n = ").place(x = out_x2-s, y = (out_y+24*7))
        tk.Label(self, text = "u|ax = ").place(x = out_x2-s, y = (out_y+24*8))
        tk.Label(self, text = "u|ax:n = ").place(x = out_x2-s, y = (out_y+24*9))
        # tk.Label(self, text = "V(ax) = ").place(x = out_x2-s, y = (out_y+24*10))
        # tk.Label(self, text = "V(ax:n) = ").place(x = out_x2-s, y = (out_y+24*11))

        tk.Label(self, text = "tpy = ").place(x = out_x3-s, y = (out_y+24*0))
        tk.Label(self, text = "tqy = ").place(x = out_x3-s, y = (out_y+24*1))
        tk.Label(self, text = "u|tqy = ").place(x = out_x3-s, y = (out_y+24*2))
        tk.Label(self, text = "ey = ").place(x = out_x3-s, y = (out_y+24*3))
        tk.Label(self, text = "ey:n = ").place(x = out_x3-s, y = (out_y+24*4))
        tk.Label(self, text = "Ay = ").place(x = out_x3-s, y = (out_y+24*5))
        tk.Label(self, text = "Ay:n = ").place(x = out_x3-s, y = (out_y+24*6))
        tk.Label(self, text = "nEy = ").place(x = out_x3-s, y = (out_y+24*7))
        tk.Label(self, text = "ay = ").place(x = out_x3-s, y = (out_y+24*8))
        tk.Label(self, text = "ay:n = ").place(x = out_x3-s, y = (out_y+24*9))

        tk.Label(self, text = "tpxy = ").place(x = out_x4-s, y = (out_y+24*0))
        tk.Label(self, text = "tqxy = ").place(x = out_x4-s, y = (out_y+24*1))
        tk.Label(self, text = "u|tqxy = ").place(x = out_x4-s, y = (out_y+24*2))
        tk.Label(self, text = "exy = ").place(x = out_x4-s, y = (out_y+24*3))
        tk.Label(self, text = "exy:n = ").place(x = out_x4-s, y = (out_y+24*4))
        tk.Label(self, text = "Axy = ").place(x = out_x4-s, y = (out_y+24*5))
        tk.Label(self, text = "Axy:n = ").place(x = out_x4-s, y = (out_y+24*6))
        tk.Label(self, text = "nExy = ").place(x = out_x4-s, y = (out_y+24*7))
        tk.Label(self, text = "axy = ").place(x = out_x4-s, y = (out_y+24*8))
        tk.Label(self, text = "axy:n = ").place(x = out_x4-s, y = (out_y+24*9))
        tk.Label(self, text = "tpxybar = ").place(x = out_x4-s, y = (out_y+24*10))
        
        

        # Output calculations
        self.output_tpx = tk.Label(self); self.output_tpx.place(x = out_x1, y = out_y+24*0)
        self.output_tqx = tk.Label(self); self.output_tqx.place(x = out_x1, y = out_y+24*1)
        self.output_utqx = tk.Label(self); self.output_utqx.place(x = out_x1, y = out_y+24*2)
        self.output_ex = tk.Label(self); self.output_ex.place(x = out_x1, y = out_y+24*3)
        self.output_2ex = tk.Label(self); self.output_2ex.place(x = out_x1, y = out_y+24*4)
        self.output_vt = tk.Label(self); self.output_vt.place(x = out_x1, y = out_y+24*5)
        self.output_exn = tk.Label(self); self.output_exn.place(x = out_x1, y = out_y+24*6)
        self.output_2exn = tk.Label(self); self.output_2exn.place(x = out_x1, y = out_y+24*7)
        self.output_vtn = tk.Label(self); self.output_vtn.place(x = out_x1+40, y = out_y+24*8)
        self.output_Ax = tk.Label(self); self.output_Ax.place(x = out_x1, y = out_y+24*9)
        self.output_2Ax = tk.Label(self); self.output_2Ax.place(x = out_x1, y = out_y+24*10)
        self.output_Vvt = tk.Label(self); self.output_Vvt.place(x = out_x1+15, y = out_y+24*11)
        self.output_Axn = tk.Label(self); self.output_Axn.place(x = out_x1, y = out_y+24*12)
        self.output_2Axn = tk.Label(self); self.output_2Axn.place(x = out_x1, y = out_y+24*13)
        self.output_Vvtn = tk.Label(self); self.output_Vvtn.place(x = out_x1+55, y = out_y+24*14)
        self.output_uAx = tk.Label(self); self.output_uAx.place(x = out_x1, y = out_y+24*15)
        self.output_uAxn = tk.Label(self); self.output_uAxn.place(x = out_x1+10, y = out_y+24*16)

        self.output_nEx = tk.Label(self); self.output_nEx.place(x = out_x2, y = out_y+24*0)
        self.output_2nEx = tk.Label(self); self.output_2nEx.place(x = out_x2, y = out_y+24*1)
        self.output_VvtIn = tk.Label(self); self.output_VvtIn.place(x = out_x2+100, y = out_y+24*2)
        self.output_A1xn = tk.Label(self); self.output_A1xn.place(x = out_x2+10, y = out_y+24*3)
        self.output_2A1xn = tk.Label(self); self.output_2A1xn.place(x = out_x2+10, y = out_y+24*4)
        self.output_VvtIt = tk.Label(self); self.output_VvtIt.place(x = out_x2+100, y = out_y+24*5)
        self.output_ax = tk.Label(self); self.output_ax.place(x = out_x2, y = out_y+24*6)
        self.output_axn = tk.Label(self); self.output_axn.place(x = out_x2, y = out_y+24*7)
        self.output_uax = tk.Label(self); self.output_uax.place(x = out_x2, y = out_y+24*8)
        self.output_uaxn = tk.Label(self); self.output_uaxn.place(x = out_x2+5, y = out_y+24*9)
        # self.output_Vax = tk.Label(self); self.output_Vax.place(x = out_x2, y = out_y+24*10)
        # self.output_Vaxn = tk.Label(self); self.output_Vaxn.place(x = out_x2, y = out_y+24*11)
        
        self.output_tpy = tk.Label(self); self.output_tpy.place(x = out_x3, y = out_y+24*0)
        self.output_tqy = tk.Label(self); self.output_tqy.place(x = out_x3, y = out_y+24*1)
        self.output_utqy = tk.Label(self); self.output_utqy.place(x = out_x3, y = out_y+24*2)
        self.output_ey = tk.Label(self); self.output_ey.place(x = out_x3, y = out_y+24*3)
        self.output_eyn = tk.Label(self); self.output_eyn.place(x = out_x3, y = out_y+24*4)
        self.output_Ay = tk.Label(self); self.output_Ay.place(x = out_x3, y = out_y+24*5)
        self.output_Ayn = tk.Label(self); self.output_Ayn.place(x = out_x3, y = out_y+24*6)
        self.output_nEy = tk.Label(self); self.output_nEy.place(x = out_x3, y = out_y+24*7)
        self.output_ay = tk.Label(self); self.output_ay.place(x = out_x3, y = out_y+24*8)
        self.output_ayn = tk.Label(self); self.output_ayn.place(x = out_x3, y = out_y+24*9)

        self.output_tpxy = tk.Label(self); self.output_tpxy.place(x = out_x4, y = out_y+24*0)
        self.output_tqxy = tk.Label(self); self.output_tqxy.place(x = out_x4, y = out_y+24*1)
        self.output_utqxy = tk.Label(self); self.output_utqxy.place(x = out_x4, y = out_y+24*2)
        self.output_exy = tk.Label(self); self.output_exy.place(x = out_x4, y = out_y+24*3)
        self.output_exyn = tk.Label(self); self.output_exyn.place(x = out_x4, y = out_y+24*4)
        self.output_Axy = tk.Label(self); self.output_Axy.place(x = out_x4, y = out_y+24*5)
        self.output_Axyn = tk.Label(self); self.output_Axyn.place(x = out_x4, y = out_y+24*6)
        self.output_nExy = tk.Label(self); self.output_nExy.place(x = out_x4, y = out_y+24*7)
        self.output_axy = tk.Label(self); self.output_axy.place(x = out_x4, y = out_y+24*8)
        self.output_axyn = tk.Label(self); self.output_axyn.place(x = out_x4, y = out_y+24*9)
        self.output_tpxybar = tk.Label(self); self.output_tpxybar.place(x = out_x4+15, y = out_y+24*10)


        # Input Labels
        tk.Label(self, text = "u = ").place(x = 20, y = 70, width = 25)
        tk.Label(self, text = "t = ").place(x = 20, y = 90, width = 25)
        tk.Label(self, text = "x | y = ").place(x = 0, y = 110, width = 50)
        tk.Label(self, text = "n = ").place(x = 20, y = 130, width = 25)
        tk.Label(self, text = "i = ").place(x = 20, y = 150, width = 25)

        # Descriptions for input variables
        tk.Label(self, text = " ---> How many years since x until t?").place(x = 200, y = 70)
        tk.Label(self, text = " ---> How many years since x + t?").place(x = 200, y = 90)
        tk.Label(self, text = " ---> How many years old are (x) and (y)?").place(x = 200, y = 110)
        tk.Label(self, text = " ---> How many years in the term?").place(x = 200, y = 130)
        tk.Label(self, text = " ---> What is the interest rate? (Ex: SULT = 1.05)").place(x = 200, y = 150)
        
        # Entries for u, t, x, n, i, y respectively
        # The "insert" additive is mysterious to me. The first argument determines the 
        # datatype: 0=string, 1=int, idk what else there is and the second is the value.
        self.e1 = tk.Entry(self, textvariable = self.e1); self.e1.place(x = 50, y = 70); self.e1.insert(1, 1) # u
        self.e2 = tk.Entry(self, textvariable = self.e2); self.e2.place(x = 50, y = 90); self.e2.insert(1, 10) # t
        self.e3 = tk.Entry(self, textvariable = self.e3, width = 10); self.e3.place(x = 50, y = 110); self.e3.insert(1, 20) # x
        self.e4 = tk.Entry(self, textvariable = self.e4); self.e4.place(x = 50, y = 130); self.e4.insert(1, 10) # n
        self.e5 = tk.Entry(self, textvariable = self.e5); self.e5.place(x = 50, y = 150); self.e5.insert(0, "1.05") # i
        self.e6 = tk.Entry(self, textvariable = self.e6, width = 10); self.e6.place(x = 110, y = 110); self.e6.insert(1, 30) # y

        # Calculation Button
        calc_btn = tk.Button(self, text="Calculate", 
                            command = lambda : self.calculate())
        calc_btn.place(x = 40, y = 35, width = 100)
        
        # Box to calculate for select lives
        self.checkvar = IntVar()
        check = tk.Checkbutton(self, text = "Select Life", variable = self.checkvar)
        check.place(x = 200, y = 35)

    # Retrieve the number of lives at age x
    def l(self, x):
        if self.checkvar.get() == 0:
            return(self.df.at[x-18,"lx"])
        if self.checkvar.get() == 1:
            self.x = int(self.e3.get())
            if x < self.x + 3 : 
                return(self.df.at[x-18,"l[x]"])
            else: 
                return(self.df.at[x-18, "lx"])
        else: return 1

    # Retrieve the number of lives at age y
    def ly(self, y):
        if self.checkvar.get() == 0:
            return(self.df.at[y-18,"lx"])
        if self.checkvar.get() == 1:
            self.y = int(self.e6.get())
            if y < self.y + 3 : 
                return(self.df.at[y-18,"l[x]"])
            else: 
                return(self.df.at[y-18, "lx"])
        else: return 1
    
    # Perform necessary calculations
    def calculate(self):

        # Define variables
        u = int(self.e1.get())
        t = int(self.e2.get())
        x = int(self.e3.get())
        n = int(self.e4.get())
        i = float(self.e5.get())
        y = int(self.e6.get())
        v = pow(i, -1)
        d = (i / (1 + i))
        self.npx = (self.l(x+n) / self.l(x))
        self.npy = (self.ly(y+n) / self.ly(y))
        self.nEx = self.npx * pow(v, n)
        self._2nEx = self.npx * pow(v, 2*n)
        self.nEy = self.npy * pow(v, n)



        ### COLUMN 1 ###
        # Equation for tpx
        self.tpx = ( ( self.l(x+t) / (self.l(x)) )\
                    if 17 < t + x + u and t + x + u < 130 else "Please input t, u, and x\n such that\n 17 < t + x + u < 130,\n where x and t are integers.")
        self.output_tpx.config(text = round(self.tpx, r))

        # Equation for tqx
        self.tqx = ( (self.l(x) - self.l(x+t)) / self.l(x)
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_tqx.config(text = round(self.tqx, r))

        # Equation for u|tqx
        self.utqx = ( ( (self.l(x+u) - self.l(x+u+t)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_utqx.config(text = round(self.utqx, r))

        # Equation for ex
        self.ex = 0
        for k in range(0, 130-x):
            self.ex += k * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_ex.config(text = round(self.ex, r))

        # Equation for 2ex
        self._2ex = 0
        for k in range(0, 130-x):
            self._2ex += pow(k,2) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_2ex.config(text = round(self._2ex, r))

        # Equation for V(Tx)
        self.output_vt.config(text = round((self._2ex - pow(self.ex, 2)), r))

        # Equation for ex:n
        self.exn = 0
        for k in range(0, n+1):
            self.exn += k * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_exn.config(text = round(self.exn, r))

        # Equation for 2ex:n
        self._2exn = 0
        for k in range(0, n+1):
            self._2exn += pow(k,2) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_2exn.config(text = round(self._2exn, r))
   
        # Equation for V(min(Tx, n))
        self.output_vtn.config(text = round((self._2exn - pow(self.exn, 2)), r))

        # Equation for Ax
        self.Ax = 0
        for k in range(0, 130-x):
            self.Ax += pow(v,(k+1)) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_Ax.config(text = round(self.Ax, r))        

        # Equation for 2Ax
        self._2Ax = 0
        for k in range(0, 130-x):
            self._2Ax += pow(v,2*(k+1)) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_2Ax.config(text = round(self._2Ax, r))        

        # Equation for V(v(Tx))
        self.output_Vvt.config(text = round((self._2Ax - pow(self.Ax, 2)), r))

        # Equation for Axn
        self.Axn = 0
        for k in range(0, n):
            self.Axn += pow(v,k+1) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_Axn.config(text = round((self.Axn + self.nEx), r))  

        # Equation for 2Axn
        self._2Axn = 0
        for k in range(0, n):
            self._2Axn += pow(v,2*(k+1)) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_2Axn.config(text = round((self._2Axn + self._2nEx), r))
   
        # Equation for V(min(Tx, n))
        self.output_Vvtn.config(text = round((self._2Axn - pow(self.Axn, 2)), r))

        # Equation for u|Ax
        self.uAx = 0
        for k in range(u, 130-x-u):
            self.uAx += pow(v,k+1) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_uAx.config(text = round(self.uAx, r))  

        # Equation for u|Axn
        self.uAxn = 0
        for k in range(u, n+u):
            self.uAxn += pow(v,k+1) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_uAxn.config(text = round(self.uAxn, r))  


        ### COLUMN 2 ###
        # Equation for nEx
        self.output_nEx.config(text = round(self.nEx, r))

        # Equation for 2nEx
        self.output_2nEx.config(text = round(self._2nEx, r))

        # Equation for V(min(v^Tx, n)*I(Tx>n))
        self.output_VvtIn.config(text = round(( self._2nEx - pow(self.nEx, 2) ), r) )

        # Equation for A1xn
        self.A1xn = 0
        for k in range(0, n):
            self.A1xn += pow(v,k+1) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_A1xn.config(text = round(self.A1xn, r))  

        # Equation for 2A1xn
        self._2A1xn = 0
        for k in range(0, n):
            self._2A1xn += pow(v,2*(k+1)) * ( ( (self.l(x+k) - self.l(x+k+1)) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_2A1xn.config(text = round(self._2A1xn, r))  
   
        # Equation for V(min(v^Tx, n)*I(Tx<n))
        self.output_VvtIt.config(text = round(( self._2A1xn - pow(self.A1xn, 2) ), r) )

        # Equation for ax
        self.ax = 0
        for k in range(0, 130-x):
            self.ax += pow(v,k) * ( ( self.l(x+k) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_ax.config(text = round(self.ax, r))  

        # Equation for axn
        self.axn = 0
        for k in range(0, n):
            self.axn += pow(v,k) * ( ( self.l(x+k) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_axn.config(text = round(self.axn, r))  

        # Equation for u|ax
        self.uax = 0
        for k in range(u, 130-x-u):
            self.uax += pow(v,k) * ( ( self.l(x+k) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_uax.config(text = round(self.uax, r)) 

        # Equation for u|axn
        self.uaxn = 0
        for k in range(u, u+n):
            self.uaxn += pow(v,k) * ( ( self.l(x+k) / self.l(x) )
                    if 17 < t + x + u and t + x + u < 130 else "")
        self.output_uaxn.config(text = round(self.uaxn, r))

        # Equation for V(ax)
        # self.Vax = (self._2Ax - pow(self.Ax , 2)) / pow((i*v), 2)
        # self.output_Vax.config(text = round(self.Vax, r))


        ##COLUMN 3##
        # Equation for tpy
        self.tpy = ( ( self.ly(y+t) / (self.ly(y)) )\
            if 17 < t + y + u and t + y + u < 130 else "Please input t, u, and x\n such that\n 17 < t + x + u < 130,\n where x and t are integers.")
        self.output_tpy.config(text = round(self.tpy, r))

        # Equation for tqy
        self.tqy = ( (self.ly(y) - self.ly(y+t)) / self.ly(y)
                if 17 < t + y + u and t + y + u < 130 else "")
        self.output_tqy.config(text = round(self.tqy, r))
        
        # Equation for u|tqy
        self.utqy = ( ( (self.ly(y+u) - self.ly(y+u+t)) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_utqy.config(text = round(self.utqy, r))
        
        # Equation for ey
        self.ey = 0
        for k in range(0, 130-y):
            self.ey += k * ( ( (self.ly(y+k) - self.ly(y+k+1)) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_ey.config(text = round(self.ey, r))

        # Equation for ey:n
        self.eyn = 0
        for k in range(0, n+1):
            self.eyn += k * ( ( (self.ly(y+k) - self.ly(y+k+1)) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_eyn.config(text = round(self.eyn, r))
        
        # Equation for Ay
        self.Ay = 0
        for k in range(0, 130-y):
            self.Ay += pow(v,(k+1)) * ( ( (self.ly(y+k) - self.ly(y+k+1)) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_Ay.config(text = round(self.Ay, r))     
        
        # Equation for Ayn
        self.Ayn = 0
        for k in range(0, n):
            self.Ayn += pow(v,k+1) * ( ( (self.ly(y+k) - self.ly(y+k+1)) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_Ayn.config(text = round((self.Ayn + self.nEy), r))  
        
        # Equation for nEy
        self.output_nEy.config(text = round(self.nEy, r))
        
        # Equation for ay
        self.ay = 0
        for k in range(0, 130-y):
            self.ay += pow(v,k) * ( ( self.ly(y+k) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_ay.config(text = round(self.ay, r))  
        
        # Equation for ayn
        self.ayn = 0
        for k in range(0, n):
            self.ayn += pow(v,k) * ( ( self.ly(y+k) / self.ly(y) )
                    if 17 < t + y + u and t + y + u < 130 else "")
        self.output_ayn.config(text = round(self.ayn, r))  


        ## COLUMN 4 ##
        # Equation for tpxy
        self.output_tpxy.config(text = round((self.tpx * self.tpy), r))

        # Equation for tqxy
        self.output_tqxy.config(text = round((1 - self.tpx * self.tpy), r))

        # Equation for u|tqxy
        self.utqxy = ( ( (self.l(x+u) - self.l(x+u+t)) * (self.ly(y+u) - self.ly(y+u+t)) / self.l(x) / self.ly(y) )
                    if 17 < t + max(x, y) + u and t + max(x, y) + u < 130 else "")
        self.output_utqxy.config(text = round(self.utqxy, r))

        # Equation for exy
        self.exy = 0
        for k in range(0, 130-max(x, y)):
            self.exy += k * ( ( (self.l(x+k) - self.l(x+k+1)) * (self.ly(y+k) - self.ly(y+k+1)) / self.l(x) / self.ly(y) )
                    if 17 < t + max(x, y) + u and t + max(x, y) + u < 130 else "")
        self.output_exy.config(text = round(self.exy, r))

        # Equation for exyn

        # Equation for Axy

        # Equation for Axyn

        # Equation for nExy

        # Equation for tpxybar
        self.output_tpxybar.config(text = round((self.tpx + self.tpy - (self.tpx * self.tpy)), r))
        
        # Equation for axy
        self.axy = 0
        for k in range(0, 130-max(x, y)):
            self.axy += pow(v,k) * ( ( ( self.l(x+k) / self.l(x) ) * ( self.ly(y+k) / self.ly(y) ) )
                    if 17 < t + max(x, y) + u and t + max(x, y) + u < 130 else "")
        self.output_axy.config(text = round(self.axy, r))  
        
        # Equation for axyn
        self.axyn = 0
        for k in range(0, n):
            self.axyn += pow(v,k) * ( ( ( self.l(x+k) / self.l(x) ) * ( self.ly(y+k) / self.ly(y) ) )
                    if 17 < t + max(x, y) + u and t + max(x, y) + u < 130 else "")
        self.output_axyn.config(text = round(self.axyn, r))  

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
    
