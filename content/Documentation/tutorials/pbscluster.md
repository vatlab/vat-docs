+++
title = "association analysis on cluster using PBS"
weight = 7
hidden = true
+++


## Run association analysis on cluster using PBS

Since vtools association analysis is quite time consuming, meanwhile this job could be easily distributed to run on multiple nodes. Here we show an example to demonstrate how to run vtools association job on cluster using PBS.

The template PBS script is `vtools_association_cluster.pbs` in `/src/variant_tools` folder. You are supposed to modify the number of nodes, number of cores according to your needs and provide values for `PROJECTFOLDER`, `COMMAND`, and `NUMBER_OF_PROCESSES_PER_NODE`. The current setup is to run main program on one node, then submit calculation tasks to the rest of nodes. Please adjust the bash script to get the node names if needed. 

Please make sure the `openmpi` module is loaded, so that `mpiexec` command could be executed.


### 1. Header of PBS script

Like any other PBS scripts, you first specify the number of nodes and cores assigned to run this job. In this example, we will use four nodes and eight cores from each node. The job will be submitted to a job queue named short.

    #!/bin/bash
    #PBS -l nodes=4:lowmem:ppn=8,walltime=01:00:00
	#PBS -V
	#PBS -q short

### 2. Specify project folder

You need to specify the folder path to the existing vtools project (The folder created by `vtools init` command) by assigning the folder path to `PROJECTFOLDER`. PROJECTFOLDER could be set as an environmental variable or given a value in the script.

### 3. Specify the vtools associate command

At this step, you should have already imported the data and added necessary annotations. Then you are required to provide the preferred vtools associate command to `COMMAND` variable. The vtools associate command line parameters are the same as running this command on local desktop with an additional flag `-mpi` to indicate the job will be ran on the cluster. 

### 4. Specify the number of processes per node

If you claim to use four nodes, one of the nodes will be used to run main program, the other three nodes will be taken as worker nodes. If you use eight cores per node, then `NUMBER_OF_PROCESSES_PER_NODE` could be set to 8. 


### 5. Submit job

After PBS script submitted with qsub, the job will be launched to run on the cluster with mpiexec, the communication between main node and worker nodes is handled through zeroMQ. The result could be viewed in output file or saved into database with `--to_db` parameter set in associate command. 


