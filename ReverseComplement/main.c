#include <stdio.h>
void setInitArr(int *arr);
int setTwoCom(int n);
void printBit(int *arr);

int arr[8];
const int MAX_SIZE =8;           


int setTwoCom(int n){
	setInitArr(arr);
	int num = n;
	int rest,i,point;
	int cur = 0;
	do{
		point=num/2;
		arr[cur++]=num%2;
		num=point;
	}while(point>0);

//	printBit(arr);
	return getValue(arr);
}
void setInitArr(int *arr){
	int i;
	for (i=0;i<MAX_SIZE;i++){
		arr[i]=0;
	}
}
int getEndIndex(int *arr){
	int i;
	for (i=MAX_SIZE-1;i>=0;i--){
		if (arr[i]==1){
			break;
		}
	}	
	return i;
}
int getValue(int *arr){
	int i,j;
	int end;
	int v;
	int tmp;
	int size=2;
	end = getEndIndex(arr);
	v=0;
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

void printBit(int *arr){
	int i;
	for (i=0;i<sizeof(arr)/sizeof(int);i++){
		printf("%d ",arr[i]);
	}
	printf("\n");

}



int main(void){
	printf("%d\n",setTwoCom(37));
	printf("%d\n",setTwoCom(54));
	printf("%d\n",setTwoCom(27));

	return 0;
}


