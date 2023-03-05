int fibo(int n){
    if(n==0){
        return 0;
    }
    else if (n==1){
        return 1;
    }
    else {
        return(fibo(n-1)+fibo(n-2));
    }
}
int main(){
    int i,n; 
    printf("entre o índice N da sequência de fibonacci desejado: ");
    scanf("%d",&n);
    printf("O valor da %dª posição da sequência de fibonacci é %d", n,fibo(n));
}
/*#include <stdio.h>
int main(){
    int i,n,t0,t1,t2; 
    t2 = 1;
    t1 = 1;
    printf("entre o índice N da sequência de fibonacci desejado: ");
    scanf("%d",&n);
    for (i=2;i<n;i++){
        t0 = t1+t2;
        t2 = t1;
        t1 = t0;
    }
    if (n==1 || n==2){
        printf("O valor da %dª posição da sequência de fibonacci é 1", n);
    }
    else{
        printf("O valor da %dª posição da sequência de fibonacci é %d", n,t0);
    }
    return 0;*/
