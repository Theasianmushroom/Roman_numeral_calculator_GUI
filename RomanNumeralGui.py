from tkinter import *

window = Tk()
window.title("NUMERAL CALCULATOR.")
window.geometry("350x125")
window.config(bg = "grey")

Values_List = []
RNT = IntVar()

def Calculations():
    Roman_Numeral_Values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    Values_List.clear()

    RN = URN.get()
    RN = RN.upper()

    def Getting_Values():
        K = False
        i = 0
        for x in RN:
            while i < len(RN):
                if RN[i] in Roman_Numeral_Values:
                    Values_List.insert(i, Roman_Numeral_Values[RN[i]])
                    i += 1
                    K = True
                elif RN[i] not in Roman_Numeral_Values:
                    i += len(RN)
                    K = False
                    
        if K == False:
            UN.delete(0,END)
            UN.insert(0,"ERROR")
        elif K == True:
            Calculating_Total()
    

    def Calculating_Total():
        global Total
        Total = 0
        i = 0

        while i < len(Values_List):
            for x in Values_List:
                if i > 0 and Values_List[i] > Values_List[i-1]:
                    Total += int(Values_List[i] - 2 * Values_List[i-1])
                    i += 1
                else:
                    Total += int(Values_List[i])
                    i += 1
            RNT.set(Total)
            UN.delete(0,END)
            UN.insert(0,str(RNT.get()))
        


    Getting_Values()


URN_Label = Label(window, text = "ENTER NUMERAL:", font=(15), bg="grey")
URN_Label.grid(column=1,row=0)

URN = Entry(window, font = (20))
URN.grid(column=2,columnspan=1,row=0)

Calc_Button = Button(window, text = "CALCULATE", bg = "light grey", padx = 15, pady =5, font =(20), command = Calculations)
Calc_Button.grid(row=4,column=1,columnspan=2, padx=5,pady=5)

UN_Label = Label(window, text="NUMERAL VALUE:", font =(20), bg="grey")
UN_Label.grid(column=1,row=3)

UN = Entry(window, font =(20))
UN.grid(column=2,row=3)


window.mainloop()