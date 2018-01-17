#include <mpi.h>
#include <iostream>

int main(int argc, char** argv) {
  MPI_Init(NULL, NULL);

  int world_rank, world_size;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  if (world_size < 2) {
    MPI_Abort(MPI_COMM_WORLD, 1);
  }
  std::cout << world_size << world_rank << std::endl;

  int ans;
  for(int i=0;i<world_size;i++) {
    if (i != world_rank) {
      MPI_Send(&world_rank, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
      std::cout << "Process "<< world_rank
		<< " sending  " << world_rank
		<< " to process " << i
		<< std::endl;
    }
  }
  for(int i=0;i<world_size;i++) {
    if (i != world_rank) {
      MPI_Recv(&ans, 1, MPI_INT,
	       i, MPI_ANY_TAG, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      std::cout << "Process "<< world_rank
		<< " received " << ans
		<< " from " << i
		<< std::endl;
    }
  }
  MPI_Finalize();
}
