def calculate_B():
        no = 1
        rs = 5
        tc = 24
        tk0 = (24+273)
        while True:
            tk = tc + 273
            l1 = float(input("Masukkan Nilai l1 = "))
            l2 = 100 - l1

            rt = l1/l2 * rs

            tc += 2
            print(f"{no}. T = {tk} K, Rt = {rt:.3f}, dT = {tk - tk0}")
            no += 1

            choice = input("Press Enter to continue or type 'q' to quit: ").strip().lower()
            print ("\n")
            if choice == 'q':
                print("Exiting program.")
                break

if __name__ == "__main__":
    calculate_B()
    
