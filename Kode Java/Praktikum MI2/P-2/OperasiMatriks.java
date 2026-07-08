public class OperasiMatriks {
    public static void main(String[] args) {
        int[][] A = {
            {1, 2},
            {3, 4}
        };

        int[][] B = {
            {4, 3},
            {2, 1}
        };

        int rows = A.length;
        int cols = A[0].length;

        int[][] sum = new int[rows][cols];
        int[][] diff = new int[rows][cols];
        int[][] skalar = new int[rows][cols];
        int skalarValue = 2;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sum[i][j] = A[i][j] + B[i][j];
                diff[i][j] = A[i][j] - B[i][j];
                skalar[i][j] = skalarValue * A[i][j];
            }
        }

        int[][] hasilKali = new int[rows][cols];
        for (int i = 0; i < rows; i++) {   
            for (int j = 0; j < cols; j++) {
                hasilKali[i][j] = 0;
                for (int k = 0; k < cols; k++) {
                    hasilKali[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        System.out.println("Penjumlahan Matriks: ");
        printMatrix(sum);
        System.out.println("Pengurangan Matriks: ");
        printMatrix(diff);
        System.out.println("Perkalian Skalar: ");
        printMatrix(skalar);
        System.out.println("Perkalian Matriks A * B: ");
        printMatrix(hasilKali);
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + "\t");
            }
            System.out.println();
        }
    }
}