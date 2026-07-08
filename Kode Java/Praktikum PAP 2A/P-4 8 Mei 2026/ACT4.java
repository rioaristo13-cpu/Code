import static java.lang.System.out;
import java.util.Scanner;

public class ACT4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int total = 0;
        out.print("Masukkan kapasitas array: ");
        int n = input.nextInt();        
        int [] angka = new int[n];
        for (int i  = 0; i < n; i++) {
            out.print("Masukkan nilai indeks ke-"+i+": ");
            angka[i] = input.nextInt();
            total += angka[i];
        }
        out.print("\n");
        out.println("Total Nilai: "+total);
        float rata2= total/n;
        out.println("Rata - rata: "+rata2);
    }
}
