import java.util.Scanner;

public class LA3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int menu;

        do {
            System.out.println("\n=== APLIKASI TABEL MATRIKS ===");
            System.out.println("1. Cetak Tabel Perkalian (Nested For)");
            System.out.println("2. Keluar");
            System.out.print("Pilih Menu: ");
            menu = input.nextInt();

            if (menu == 1) {
                System.out.print("Masukkan ukuran tabel (Max 10): ");
                int size = input.nextInt();

                System.out.println("\n--- TABEL PERKALIAN " + size + "x" + size + " ---");

                for (int i = 1; i <= size; i++) {
                    for (int j = 1; j <= size; j++) {
                        System.out.print((i * j) + "\t");
                    }
                    System.out.println();
                }
            } else if (menu != 2) {
                System.out.println("Menu tidak valid!");
            }

        } while (menu != 2);

        System.out.println("Terima kasih telah menggunakan program ini.");
        input.close();
    }
}