#include <stdio.h>
void setInitArr();
void setTwoCom(int n);

int arr[8];


void setTwoCom(int n){
	setInitArr();
	int num = n;
	int rest,i,point;
	//int cur=(sizeof(arr)/sizeof(int))-1;
	int cur = 0;
	do{
		point=num/2;
		arr[cur++]=num%2;
		num=point;
	}while(point>0);
}
void reverseCom(){
	int i;

	for (i=0;i<sizeof(arr)/sizeof(int);i++){

		arr[i]= ( arr[i]==1 ) ? 0:1;
	}
}
void setInitArr(){
	int i;
	for (i=0;i<sizeof(arr)/sizeof(int);i++){
		arr[i]=0;
	}
}
int getValue(){
	int i,j;
	int end;
	int v;
	int tmp;
	int size;
	for (i=sizeof(arr)/sizeof(int);i>=0;i--){
		if (arr[i]==1){
			end=i;
			break;
		}
	}	
	size=2;	
	for (i=end;i>=0;i--){
		tmp= (arr[i]==1)?0:1;
		if (i==end){
			v+=tmp;
		}else{
			for(j=1;j<size;j++){
				tmp*=2;
			}		
			v+=tmp;
			size++;
		}
	}	
	return v;
}

void printArr(){
	int i;
	for (i=0;i<sizeof(arr)/sizeof(int);i++){
		printf("%d ",arr[i]);
	}
	printf("\n");

}



int main(void){
	int i;
	setTwoCom(27);	
//	reverseCom();
	printArr();
	printf("value:%d\n",getValue());

	return 0;
}


