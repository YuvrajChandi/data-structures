package sorting;

public class QuickSort {
    public static void printArray(int[] arr){
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        int i =0;

        for(int ele:arr){
            sb.append(ele);
            i++;
            if(i<arr.length) sb.append(", ") ;

        }
        sb.append(']');
        System.out.println(sb);


    }
    public static int partition(int[] arr, int low, int high){
        int pivot = arr[high];
        int i = low-1;
        for(int j = low;j<high;j++){
            if(arr[j]<pivot){
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

            }
        }
        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;
    

        return i+1;

    }

    public static int[] quickSort(int[] arr,int low, int high){
        if(low<high){
            int pi = partition(arr,low,high);
            quickSort(arr,low,pi-1);
            quickSort(arr,pi+1,high);

        }


        return arr;
    }
    public static void main(String args[]){
        int[] arr = {3,7,2,7,3,6,9,3,8};
        printArray(arr);
        quickSort(arr,0,arr.length-1);
        printArray(arr);




    }
    
}