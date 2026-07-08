def calculate_A():
        no = 1
        t0 = 28
        sdT = 0
        st = 0
        st2 = 0
        sdTxt = 0 
        while True:
            tn = float(input("Masukkan nilai T = "))
            m = float(input("Masukkan t(menit) = "))
            dT = tn - t0
            t = (m*60)
            print(f"{no}.dT = {dT}, t = {t}, t^2 = {t**2},  dT.t = {dT*t}")

            no += 1
            sdT += dT
            st += t 
            st2 += t**2 
            sdTxt += dT*t


            choice = input("\tPress Enter to continue or type 'q' to quit: ").strip().lower()
            print ("\n")
            if choice == 'q':
                print(f"sdT = {sdT}, st = {st}, t^2 = {st2},  dT.t = {sdTxt}")
                break


if __name__ == "__main__":
    calculate_A()
    
