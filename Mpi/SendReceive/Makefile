run:    a.out
	salloc -N4 --ntasks-per-node=1 mpirun --bind-to none ./a.out

a.out: send_recv.cpp
	mpic++ send_recv.cpp

