package sorting;
//bubble
//quick 
//selection 
//insertion


public class BubbleSort {
    public static int[] bubbleSort(int[] arr){
       
        for(int i =0;i<arr.length;i++){
            for(int j=0;j<arr.length-i-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }


        return arr;

    }
    
    public static void printArray(int[] arr) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        int i = 0;
        for(int ch: arr) {
            sb.append(ch);
            i++;
            if(i < arr.length) {
                sb.append(", ");
            }
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
    public static void main(String[] args) {
        int[] arr = {3,2,6,3,8,4,6,4,0};
        printArray(arr);
        bubbleSort(arr);
        printArray(arr);


    }
}