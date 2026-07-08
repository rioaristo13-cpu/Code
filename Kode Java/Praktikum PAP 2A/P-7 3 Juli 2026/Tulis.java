import java.io.*;
import static java.lang.System.out;
import java.util.Scanner;

public class Tulis {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String path = "FolderBelajar";
        
        try {
            File dir = new File(path);
            if (!dir.exists()) {
                dir.mkdir();
            }

            File fileData = new File(dir, "data_nilai.txt");
            PrintStream diskwriter = new PrintStream(fileData);

            out.print("Masukkan Nama : ");
            String nama = input.nextLine();
            out.print("Masukkan Nilai (Angka) : ");
            int nilai = input.nextInt();

            String grade = (nilai >= 80) ? "A" : (nilai >= 60) ? "C" : "E bjir";
            String keterangan = (nilai >= 60 )? "Lulus" : "Tidak Lulus";

            diskwriter.println("Nama : " + nama + ", Nilai : " + nilai + ", Grade : " + grade + ", Ket : " + keterangan);
            diskwriter.close();
            out.println("Data berhasil disimpan ke file!\n");

            if (fileData.exists()) {
                out.println("Nama File : " + fileData.getName());
                out.println("Path : " + fileData.getAbsolutePath());
                out.println("Ukuran : " + fileData.length() + " bytes");
                out.println("Bisa Dibaca ? : " + fileData.canRead());
            }

        } catch (FileNotFoundException e) {
            System.out.println("File tidak ada : " + e.getMessage());

        } finally {
            input.close();
        }
    }    
}