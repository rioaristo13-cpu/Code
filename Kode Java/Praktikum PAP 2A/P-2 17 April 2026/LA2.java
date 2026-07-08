import static java.lang.System.out;
import java.util.Scanner;

public class LA2 { 
    public static void main(String[] args) {
        while (true) {
            Scanner input = new Scanner(System.in);

            out.println("\n=== MENU PROGRAM PERCABANGAN ===");
            out.println("1. Biodata");
            out.println("2. Kalkulator");
            out.println("3. Grade Nilai");
            out.println("4. Exit menu");
            out.print("Pilih Menu (1-4) : ");
            int menu = input.nextInt();
            input.nextLine();

            switch (menu) {
                case 1:
                    out.print("Masukkan Nama \t  : ");
                    String nm = input.nextLine();
                    out.print("Masukkan Kelas \t  : ");
                    String kls = input.nextLine();
                    out.print("Masukkan NPM \t  : ");
                    String npm = input.nextLine();
                    out.print("Masukkan Jurusan  : ");
                    String jur = input.nextLine();
                    out.print("Masukkan Fakultas : ");
                    String fak = input.nextLine();

                    out.println("\n--- Output Biodata ---");
                    out.println("Nama Anda adalah \t: " + nm);
                    out.println("Kelas Anda adalah \t: " + kls);
                    out.println("NPM Anda adalah \t: " + npm);
                    out.println("Jurusan Anda adalah \t: " + jur);
                    out.println("Fakultas Anda adalah \t: " + fak);
                    break;
                case 2:
                    out.println("\n--- Kalkulator ---");
                    out.print("Masukkan angka 1 : ");
                    float x1 = input.nextFloat();
                    out.print("Masukkan angka 2 : ");
                    float x2 = input.nextFloat();

                    out.println("\nPenjumlahan : " + (x1 + x2));
                    out.println("Pengurangan : " + (x1 - x2));
                    out.println("Perkalian   : " + (x1 * x2));
                    out.println("Pembagian   : " + (x1 / x2));
                    out.println("Modulus     : " + (x1 % x2));
                    break;
                case 3:
                    out.println("\n--- Grade Nilai ---");
                    out.print("Masukkan Nilai UTS : ");
                    float n_uts = input.nextFloat();
                    out.print("Masukkan Nilai UAS : ");
                    float n_uas = input.nextFloat();

                    out.println("\n--- Output Grade Nilai ---");
                    out.println("Nilai UTS   \t: " + n_uts);
                    out.println("Nilai UAS   \t: " + n_uas);
                    float n_rata = (n_uts + n_uas) / 2;
                    out.println("Rata - Rata \t: " + n_rata);

                    if        (n_rata >= 90) {
                        out.println("Grade\t\t: Baik Sekali");
                    } else if (n_rata >= 80) {
                        out.println("Grade\t\t: Baik ");
                    } else if (n_rata >= 70) {
                        out.println("Grade\t\t: Cukup Baik");                        
                    } else if (n_rata >= 60) {
                        out.println("Grade\t\t: Kurang");
                    } else {
                        out.println("Grade\t\t: Kurang Sekali");
                    }                  
                    break;
                case 4:
                    out.println("\nTerima Kasih");
                    input.close();
                    return;
                default: 
                    out.println("\nMenu Tidak Tersedia. ");
            }
        }
    }
}

//90 - 100 Sangat baik
//80 - 89 Baik
//70 - 79 Cukup baik
//60 - 69 Kurang
//<60 Kurang Sekali
