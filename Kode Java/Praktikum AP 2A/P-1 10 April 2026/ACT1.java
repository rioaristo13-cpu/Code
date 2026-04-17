import static java.lang.System.out;
import java.util.Scanner;

public class ACT1 {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        out.print("Masukkan bilangan pertama : ");
        int bil1 = input.nextInt();

        out.print("Masukkan bilangan kedua : ");
        int bil2 = input.nextInt();

        int jumlah  = bil1 + bil2;
        int kurang  = bil1 - bil2;
        int kali    = bil1 * bil2;
        int bagi    = bil1 / bil2;

        out.println(bil1 + " + " + bil2 + " = " + jumlah);
        out.println(bil1 + " - " + bil2 + " = " + kurang);
        out.println(bil1 + " * " + bil2 + " = " + kali);
        out.println(bil1 + " / " + bil2 + " = " + bagi);        
        input.close();
    }
}
