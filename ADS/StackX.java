package ADS ;

public class StackX{
    
    public static int push(int[] st,int top,int value){
        if(top==st.length) System.out.println("overflow");
        st[top]=value;
        top++;
        display(st,top);
        return top;
        
    }
    public static int pop(int[] st, int top){
        if(top==-1) System.out.println("Underflow");
        st[top] = 0;
        top--;
        display(st,top);
        
        
        return top;
        
        
    }
    
    public static void display(int[] st, int top) {
        System.out.print("[ ");
        for (int i = 0; i < top; i++) {  
            System.out.print(st[i] + " ");
        }
        System.out.println("]");
    }
    
    
    public static void main(String args[]){
        int[] st = new int[10];
        int top=0;
        top=push(st,top,10);
        
        top=push(st,top,5);
        top=push(st,top,3);
        
        top=pop(st,top);
        
        
        
        
        
        
    }
}