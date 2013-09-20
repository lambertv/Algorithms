//Alg2.java
//Program by Valerie Lambert

/* Given lists C and S of n and m inegers in the range [0,k], we must
 * preprocess C and S in O(n+m+k) time so that, given a and b in [0,k],
 * we can outputthe number of integersin C in the range [a,b] and the
 * number of integers in S in [a,b] in O(1) time.
 */

import java.util.Random;

public class Alg2 {

    private int K = 1000;

    int[] create_array(int size) {
        int[] arr = new int[size];
        Random generator = new Random();
        for (int i = 0; i < size; i++) {
            arr[i] = generator.nextInt(K)+1;
        }
        return arr;
    }

    void printarr(int[] arr) {
        System.out.print("\n[ ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println("]");
    }

    int[] preprocess1(int[] arr) {
        int[] newarr = new int[K+1];
        for (int i = 0; i < arr.length; i++) {
            newarr[arr[i]]++;
        }
        return newarr;
    }

    int[] preprocess2(int[] arr) {
        int[] newarr = new int[K+1];
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            count += arr[i];
            newarr[i] = count;
        }
        return newarr;
    }

    public static void main(String[] args) {
        System.out.println("Hello!");
        Alg2 foo = new Alg2();
        int k = foo.K;
        Random generator = new Random();
        int n = generator.nextInt(k)+1;
        int m = generator.nextInt(k - n)+n;
        int[] arr1 = foo.create_array(n);
        int[] arr2 = foo.create_array(m);
        foo.printarr(arr1);
        foo.printarr(arr2);
        int[] a1 = foo.preprocess1(arr1);
        int[] a2 = foo.preprocess2(a1);
        int[] b1 = foo.preprocess1(arr2);
        int[] b2 = foo.preprocess2(b1);
        for (int i = 0; i < 100; i++) {
            int a = generator.nextInt(k)+1;
            int b = generator.nextInt(k - a + 1) + a;
            int c = a1[a] + a2[b] - a2[a];
            int s = b1[a] + b2[b] - b2[a];
            System.out.println("Elements in C in the range [" + a + ", " + b + "] is " + c);
            System.out.println("Elements in S in the range [" + a + ", " + b + "] is " + s + "\n");
        }
    }
}
