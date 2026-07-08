import java.io.*;
import static java.lang.System.out;

public class Baca {
    public static void main(String [] args) {
        String path = "FolderBelajar";
        File dir = new File(path);
        File file = new File(dir, "data_nilai.txt");

        try {
            if (file.exists()) {
                BufferedReader in = new BufferedReader(new FileReader(file));
                String baris;
                out.println("Isi dokumen " + file.getName() + ":");
                while ((baris = in.readLine()) != null) {
                    out.println(baris);
                }
                in.close();
            } else {
                out.println("File tidak ditemukan");
            }

            out.println("\nDirektori " + dir.getPath());
            if (dir.isDirectory()) {
                File[] files = dir.listFiles();
                if (files != null) {
                    for (File f : files) {
                        out.println("- " + f.getName() + " (" + f.length() + " bytes)");
                    }
                }
            }
        } catch (FileNotFoundException e) {
            out.println("File tidak ditemukan : " + e.getMessage());
        } catch (IOException e) {
            out.println("Terjadi kesalahan IO : " + e.getMessage());
        }
    }
}
