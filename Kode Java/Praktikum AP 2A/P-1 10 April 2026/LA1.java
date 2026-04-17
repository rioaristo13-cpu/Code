import static java.lang.System.out;
import java.util.Scanner;

public class LA1 {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        out.println("------------------------------------ LA1 PAP2A ------------------------------------");
        out.print("Masukan Nama\t\t: ");
        String nama = input.nextLine();
        out.print("Masukan NPM\t\t: ");
        String npm = input.nextLine();
        out.print("Masukan Kelas\t\t: ");
        String kelas = input.nextLine();
        out.print("Masukan Jurusan\t\t: ");
        String jurusan = input.nextLine();
        out.print("Masukan Fakultas\t: ");
        String fakul = input.nextLine();
        out.print("Masukan Nilai UTS\t: ");
        int nuts = input.nextInt();
        out.print("Masukan Nilai UAS\t: ");
        int nuas = input.nextInt();
        int nilaiAkhir = (nuts + nuas) / 2;
        input.close();

        out.println("===================================================================================");
        out.print("Berikut Data Diri Anda \n");

        out.println("Nama\t\t :" + nama);
        out.println("NPM\t\t :" + npm);
        out.println("Kelas\t\t :" + kelas);
        out.println("Jurusan\t\t :" + jurusan);
        out.println("Fakultas\t :" + fakul);
        out.println("Nilai UTS\t :" + nuts);
        out.println("Nilai UAS\t :" + nuas);
        out.println("Nilai Akhir\t :" + nilaiAkhir);

        out.println("===================================================================================");
    }
    
}
