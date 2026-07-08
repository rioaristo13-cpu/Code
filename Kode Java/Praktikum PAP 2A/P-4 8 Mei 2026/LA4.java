import java.util.Scanner;

public class LA4 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Masukkan jumlah baris: ");
        int baris = s.nextInt();
        System.out.print("Masukkan jumlah kolom: ");
        int kolom = s.nextInt();

        int[][] matriks = new int[baris][kolom];

        for (int i = 0; i < baris; i++) {
            for (int j = 0; j < kolom; j++) {
                System.out.print("Isi Matriks [" + i + "][" + j + "]: ");
                matriks[i][j] = s.nextInt();
            }
        }

        System.out.println("\nOutput Matriks " + baris + "x" + kolom + ":");
        for (int i = 0; i < baris; i++) {
            for (int j = 0; j < kolom; j++) {
                System.out.print(matriks[i][j] + "\t");
            }
            System.out.println();
        }

        s.close();
    }
}