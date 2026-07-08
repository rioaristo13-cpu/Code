import static java.lang.System.out;
import java.util.Scanner;

public class ACT2 {
    public static void main(String[] args) {
        while (true) {
            Scanner input = new Scanner(System.in);

            out.println ("\n=== Program Cek Status Kelulusan ===");
            out.println("1. Masukkan Nilai");
            out.println("2. Keluar");
            out.print("Pilih Menu (1 || 2) : ");
            int menu = input.nextInt();

            switch (menu) {
                case 1 -> {
                    out.print("\nMasukkan Nilai : ");
                    int nilai = input.nextInt();

                    if (nilai >= 60) {
                        out.println("\nSelamat, anda LULUS");
                    } else {
                        out.println("\nAnda TIDAK Lulus");
                    }
                }
                case 2 -> {
                    out.println("\nTerima Kasih");
                    input.close();
                    return;
                }
                default -> { 
                    out.println("\nMenu Tidak Tersedia. ");
                }
            }
        }
    }
}
