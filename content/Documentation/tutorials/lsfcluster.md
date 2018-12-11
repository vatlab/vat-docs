+++
title = "association analysis on cluster using LSF"
weight = 7
hidden = true
+++


## Run association analysis on cluster using LSF

Here we show an example to demonstrate how to run vtools association job on a cluster using LSF.

The template LSF script is `vtools_association_cluster.lsf` in `/src/variant_tools` folder. You are supposed to modify the number of nodes, number of cores according to your needs and provide values for `PROJECTFOLDER`, `COMMAND`, and `NUMBER OF PROCESSES`.
Please make sure the `openmpi` module is loaded, so that `mpiexec` command could be executed.

### 1. Header of LSF script

Like any other LSF scripts, you first specify the number of nodes and cores assigned to run this job. In this example, we will use four nodes and eight cores from each node. The job will be submitted to a job queue named short.

	#!/bin/bash
	#BSUB -W 1:00
	#BSUB -n 32
	#BSUB -N
	#BSUB -M 16384
	#BSUB -R "span[ptile=8]"
	#BSUB -q short


### 2. Specify project folder

You need to specify the folder path to the existing vtools project (The folder created by `vtools init` command) by assigning the folder path to `PROJECTFOLDER`. PROJECTFOLDER could be set as an environmental variable or given a value in the script.

### 3. Specify the vtools associate command

At this step, you should have already imported the data and added necessary annotations. Then you are required to provide the preferred vtools associate command to `COMMAND` variable. The vtools associate command line parameters are the same as running this command on local desktop with an additional flag `-mpi` to indicate the job will be ran on the cluster. 

### 4. Specify the total number of processes

If you claim to use four nodes, one of the nodes will be used to run main program, the other three nodes will be taken as worker nodes. If eight cores per node are claimed, then you could run maximum of 3x8=24 processes. The `NUMBER_OF_PROCESSES` variable could be set to 24 in this case. 

### 5. Submit job

After LSF script submitted with bsub, the job will be launched to run on the cluster with mpiexec, the communication between main node and worker nodes is handled through zeroMQ. The result could be viewed in output file or saved into database with `--to_db` parameter set in associate command. 
