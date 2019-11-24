/* Waqas Hamid */
/* beginner007*/

#include<bits/stdc++.h>
#define LL long long int
#define INF 1e18

using namespace std;

void buildMinSegTree(LL arr[], LL segtree[], LL n)
{
	LL i;
	for(i=n;i<2*n;i++)
	segtree[i]=arr[i-n];
	for(i=n-1;i>=0;i--)
	segtree[i]=min(segtree[2*i],segtree[2*i+1]);
}

void buildMaxSegTree(LL arr[], LL segtree[], LL n)
{
		LL i;
	for(i=n;i<2*n;i++)
	segtree[i]=arr[i-n];
	for(i=n-1;i>=0;i--)
	segtree[i]=max(segtree[2*i],segtree[2*i+1]);
}

void updateMinTree(LL segtree[],LL n, LL idx, LL val)
{
	segtree[n+idx] = val;
	idx+=n;
	while(idx)
	{
		idx/=2;
		segtree[idx] = min(segtree[2*idx], segtree[2*idx+1]);
	}

}

LL RMinQ(LL segtree[],LL n, LL left, LL right)
{
	left = left + n;
	right = right + n;
	LL minElement = INF;

	while(left<right)
	{
		if(left % 2 != 0)
		minElement = min(minElement, segtree[left]);
		if(right % 2 != 0)
		minElement = min(minElement, segtree[right]);
		left/=2;
		right/=2;
	}

	return minElement;
}

LL RMaxQ(LL segtree[],LL n, LL left, LL right)
{
	left = left + n;
	right = right + n;
	LL maxElement = 0;

	while(left<right)
	{
		if(left % 2 != 0)
		maxElement = max(maxElement, segtree[left]);
		if(right % 2 != 0)
		maxElement = max(maxElement, segtree[right]);
		left/=2;
		right/=2;
	}

	return maxElement;
}

int main()
{
	LL n,i;
	cin>>n;

	LL arr[n];
	LL segtree[2*n];

	for(i=0 ; i<n ; i++)
	cin>>arr[i];

	buildMinSegTree(arr,segtree,n);

	for(i=0 ; i<2*n ; i++)
	cout<<segtree[i]<<" ";

	updateMinTree(segtree, 8, 4, 1);

	cout<<endl;
	for(i=0;i<2*n;i++)
	cout<<segtree[i]<<" ";

	cout<<endl;
	cout<<RMinQ(segtree,4 , 3, 9)<<endl;

	buildMaxSegTree(arr,segtree,n);

	for(i=0 ; i<2*n ; i++)
	cout<<segtree[i]<<" ";

	cout<<endl<<RMaxQ(segtree,4 , 3, 9)<<endl;

}
