public class InversMatriks2x2 {
    
    // Fungsi untuk menghitung determinan 2x2
    public static int determinan(int[][] m) {
        return m[0][0] * m[1][1] - m[0][1] * m[1][0];
    }

    // Fungsi untuk menghitung invers 2x2
    public static double[][] invers(int[][] m) {
        int det = determinan(m);
        if (det == 0) {
            System.out.println("Matriks tidak memiliki invers karena determinan = 0.");
            return null;
        }

        double[][] hasil = new double[2][2];

        // Tukar posisi a <-> d, dan ubah tanda b dan c
        hasil[0][0] = m[1][1] / (double) det; // d / det
        hasil[0][1] = -m[0][1] / (double) det; // -b / det
        hasil[1][0] = -m[1][0] / (double) det; // -c / det
        hasil[1][1] = m[0][0] / (double) det; // a / det

        return hasil;
    }

    // Fungsi untuk mencetak matriks double
    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            for (double val : row) {
                System.out.printf("%.2f\t", val);
            }
            System.out.println();
        }
    }

    // Fungsi untuk transpose
    public static int[][] transpose(int[][] m) {
        int[][] t = new int[2][2];
        t[0][0] = m[0][0];
        t[0][1] = m[1][0];
        t[1][0] = m[0][1];
        t[1][1] = m[1][1];
        return t;
    }

    public static void main(String[] args) {
        int[][] A = {
            { 4, 7 },
            { 2, 6 }
        };

        // 1. Hitung Determinan
        int detA = determinan(A);
        System.out.println("Determinan A: " + detA);

        // 2. Hitung Invers
        double[][] A_inv = invers(A);
        if (A_inv != null) {
            System.out.println("Invers A: ");
            printMatrix(A_inv);

            // 3. Hitung determinan invers = 1/det
            System.out.printf("Determinan dari A^-1: %.2f\n", 1.0 / detA);
        }

        // 4. Transpose A
        int[][] transA = transpose(A);
        System.out.println("Transpose A: ");
        for (int[] row : transA) {
            for (int val : row) {
                System.out.print(val + "\t");
            }
            System.out.println();
        }
    }
}
