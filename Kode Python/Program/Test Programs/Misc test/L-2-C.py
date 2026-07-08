from math import log

def calculate_C():
        no = 1
        dT = 0
        slnRt, sdT, sdT2, slnxRt = 0, 0, 0, 0
        while True:
            rt = float(input("Masukkan Nilai Rt = "))
            lnrt = log(rt)
            
            print (f"{no}. \tlnRt = {lnrt:.3f}, \n\tdT = {dT}, \n\tdT^2 = {dT**2}, \n\tlnRt.dT = {lnrt*dT:.3f}")

            no += 1
            dT += 2

            slnRt += lnrt
            sdT += dT
            sdT2 += dT**2
            slnxRt += lnrt*dT

            choice = input("Press Enter to continue or type 'q' to quit: ").strip().lower()
            print ("\n")
            if choice == 'q':
                print(f"slnRt = {slnRt:.3f}, \nsdT = {sdT}, \nsdT2 = {sdT2}, \nslnRt.dT = {slnxRt:.3f}")

                y = slnRt
                x = sdT
                x2 = sdT2
                xy = slnxRt

                a = (x2*y - x*xy ) / (10*x2 - (x**2))
                b = (10*xy - x*y) / (10*x2 - (x**2))

                print(f"Nilai dari a = {a:.3f} = lnRo")
                print(f"Nilai dari b = {b:.3f} = Koefisien Temperatur")
                print("Exiting program.")
                break

if __name__ == "__main__":
    calculate_C()