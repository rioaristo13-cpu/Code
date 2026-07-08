import static java.lang.System.out;
import java.util.Scanner;

public class ACT3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
            String pilihan = "y";

        while (pilihan.equalsIgnoreCase("y")) {
            out.print("Masukkan batas angka untuk dijalankan: ");
            int batas = input.nextInt();
            int total = 0;

            out.println("Proses Penjumlahan: ");
            for (int i = 1; i <= batas; i++) {
                total += i;
                out.print(i + (i == batas ? "" : " + "));
            }

            out.println("\nTotal Akhir : " + total);

            out.print("\nApakan ingin mencoba lagi? (y/n): ");
            pilihan = input.next();
        }
        out.println("Program Selesai. Terimakasih!");
        input.close();
    }
}
