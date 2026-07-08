def calculate_A():
        no = 1
        crx = 0
        crx2 = 0
        Rs = 100

        while True:
            l1 = float(input("Enter l1 value: "))
            l2 = 100-l1

            Rx = (l1 / l2) * Rs
            print(f"{no}.Rs = {Rs}, Rx = {Rx}, Rx2 = {Rx**2}")

            no += 1
            crx += Rx
            crx2 += (Rx**2)

            choice = input("\tPress Enter to continue or type 'q' to quit: ").strip().lower()
            print ("\n")
            if choice == 'q':
                print (f"Total Rx = {crx}")
                print (f"Total Rx^2 = {crx2}")
                print("Exiting program.")
                break

            Rs += 100

if __name__ == "__main__":
    calculate_A()
    
