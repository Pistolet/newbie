##http://codingdojang.com/scode/401?answer=10422#answer_10422

#�켱 n�ڸ����� �յ� ���� ���� ����� ����ϴ� �Լ��� ����.
  a <- function(n){
    if(n==1){
      return(10)     #1�ڸ����� 10����.
    } else {
      if(n==2){
        return(9)    #2�ڸ���(11~99)�� 9����.
        } else {
          m <- n%/%2
          if(n%%2==1){    #3,5,7,9,...�ڸ����� ���
            return((10**m-10**(m-1)) * a(1))
            } else {      #4,6,8,10,...�ڸ����� ���
              return(10**m-10**(m-1)) 
            }}}}
#�ٵ� n�� 617~619�� �� Inf�� ������, 620�̻��̸� NaN�� ����. 
#R�� �������� �� �Լ��� �������� Ȯ�� �� ��. ������ 617�ڸ��� �̸����� ���� ���� ������ ��.

#�� �Լ�a(n)�� �̿��ؼ� m��° �յ� ���� ���� ����ϴ� �Լ��� ����.
apdui<-function(m){
  if(m<=10){
    return(m-1)
  }else{
k<-a(1)
i<-2
while(m>k){
  k<-k+a(i)
  i<-i+1
}
if(i%%2==1){
r<-10**((i-1)/2-1)-1+m-k+a(i-1)
result<-r
c<-trunc(log10(r))
for(h in 1:(c+1)){
  result<-paste0(result,r%%10)
  r<-r%/%10
}
return(result)
}else{
r1<-(m-k+a(i-1))%/%10+10**((i-2)/2-1)
r2<-((m-k+a(i-1)))%%10-1
result<-paste0(r1, r2)
c<-trunc(log10(r1))
for(h in 1:(c+1)){
  result<-paste0(result,r1%%10)
  r1<-r1%/%10
}
return(result)
}}}

apdui(1000000)