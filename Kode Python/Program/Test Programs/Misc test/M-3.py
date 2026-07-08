def m3_1():
        n = 0
        Ipmt = 0
        m = float(input("\nMasukkan nilai m = "))
        g = 1000
        pi = 3.14
        print("\n-----------------------------------")
        while True:
            al = input("Masukkan huruf (Ipm A/B/C/D) = ")
            l = float(input(f"Masukkan Nilai L{al} = ... Cm = "))
            t = float(input(f"Masukkan Nilai t{al} = ... sekon = "))
            p = t/10

            print(f"\n\tP{al} = t{al} / 10 = {t} / 10 = {p:.3f}")
            print(f"\n\tI{al} = P{al}^2 . m . g . l{al} / 4pi^2")
            print(f"\n\tI{al} = {p:.3f}^2 . {m} . {g} . {l} / 4pi^2")
            
            p2 = p**2
            mgl = m*g*l
            pi2 = pi**2
            pi4 = 4*pi2

            print(f"\tI{al} = {p2:.3f} . {mgl} / 4(3.14)^2")
            print(f"\tI{al} = {p2:.3f} . {mgl} / 4({pi2:.3f})")
            print(f"\tI{al} = {p2:.3f} . {mgl} / {pi4:.3f}")
            i = (p2*mgl)/pi4
            print(f"\tI{al} = {p2*mgl:.3f} / {pi4:.3f} = {i:.3f}")

            print(f"\n\tIpm{al} = I{al} - ml{al}^2 = {i:.3f} - {m}({l})^2")
            print(f"\tIpm{al} = {i:.3f} - {m*l**2}")
            ipm = i - (m*(l**2))
            print(f"\tIpm{al} = {ipm:.3f}")

            Ipmt += ipm
            n += 1

            choice = input("\nKlik Enter untuk lanjut atau ketik 'q' untuk keluar: ").strip().lower()
            print("\n")
            if choice == 'q':
                print(f"Ipmtot = {Ipmt:.3f}/{n} = {Ipmt/n:.3f}")
                print("\n-----------------------------------")
                break

def m3_2():
    print("\n--------------------------")
    pi = 3.14
    a = float(input("Masukkan nilai a = "))
    b = float(input("Masukkan nilai b = "))
    c = float(input("Masukkan nilai c = "))
    r = float(input("Masukkan nilai r = "))
    m = float(input("Masukkan nilai m (gr) = "))
    l1 = float(input("Masukkan nilai l1 = "))
    l2 = float(input("Masukkan nilai l2 = "))
    l3 = float(input("Masukkan nilai l3 = "))
    print("\n-----------------------------\n")

    print(f"m1 = ({a}x{c} / (1/2) {a}({b}+{c}) - {pi}x{r}^2) x {m}")
    print(f"m1 = ({a*c} /  {0.5*a}({b+c}) - {pi}x{r**2}) x {m}")
    print(f"m1 = ({a*c} /  {0.5*a*(b+c)} - {pi*(r**2)}) x {m}")
    print(f"m1 = ({a*c} /  {(0.5*a*(b+c)) - (pi*(r**2))}) x {m}")
    print(f"m1 = ({((a*c)/((0.5*a*(b+c)) - (pi*(r**2)))):.3f}) x {m}")
    m1 = (a*c)/((0.5*a*(b+c)) - (pi*r**2))*m
    print(f"m1 = {m1:.3f}")

    print(f"\nm2 = ({a}x({b}+{c}) / {a}({b}+{c}) - 2({pi})x{r}^2) x {m}")  
    m2 = (a*(b+c))/(a*(b+c) - 2*pi*r**2)*m
    print(f"m2 = {m2:.3f}")

    print(f"\nm3 = ({pi}x{r}^2 / (1/2) {a}({b}+{c}) - {pi}x{r}^2) x {m}")   
    m3 = (pi*r**2)/(0.5*a*(b+c)-pi*r**2)*m
    print(f"m3 = {m3:.3f}")      

    ipm1 = (1/12)*m1*(a**2+b**2)
    ipm2 = (1/18)*m2*(a**2+b**2)
    ipm3 = (1/2)*m3*(r**2)

    print(f"\nIpm1 = 1/12 {m1:.3f} ({a}^2 + {b}^2) = {ipm1:.3f}")
    print(f"Ipm2 = 1/18 {m2:.3f} ({a}^2 + {b}^2) = {ipm2:.3f}")
    print(f"Ipm3 = 1/2 {m3:.3f} {r}^2 = {ipm3:.3f}")

    ipm = ipm1 + ipm2 + ipm3 + (m1*l1**2) + (m2*l2**2) - (m3*l3**2) 
    print(f"\nIpm = {ipm1:.3f} + {ipm2:.3f} + {ipm3:.3f} + ({m1:.3f}*{l1}^2) + ({m2:.3f}*{l2}^2) - ({m3:.3f}*{l3}^2) = {ipm:.3f}")
    

if __name__ == "__main__":
    m1 = 0
    while m1 != 3:
        m1 = int(input(
"""
Pilih menu 
1. Momen I fisis
2. Momen I matematis
3. Keluar
Masukkan angka yang sesuai = """))
        match m1:
            case 1:
                m3_1()
            case 2:
                m3_2()
            case 3:
                print("\nSelesai")
            case _:
                print("\nSalah")
