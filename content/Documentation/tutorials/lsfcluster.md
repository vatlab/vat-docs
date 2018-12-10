+++
title = "association analysis on cluster using LSF"
weight = 7
hidden = true
+++


## Run association analysis on cluster using LSF

Here we show an example to demonstrate how to run vtools association job on a cluster using LSF.

The example LSF script is `vtools_association_cluster.lsf` in `/src/variant_tools` folder. 
Please make sure the `openmpi` module is loaded, so that `mpiexec` command could be executed.

### 1. Header of LSF script

Like any other LSF scripts, user first specifies the number of nodes and cores assigned to run this job. In this example, we will use four nodes and eight cores from each node. The job will be submitted to a job queue named short.

	#!/bin/bash
	#BSUB -W 1:00
	#BSUB -n 32
	#BSUB -N
	#BSUB -M 16384
	#BSUB -R "span[ptile=8]"
	#BSUB -q short


### 2. Specify project folder

User needs to specify the folder path to the existing vtools project (The folder created by `vtools init` command) by assigning the folder path to `PROJECTFOLDER`. 

### 3. Specify the vtools association command

At this step, user should have already imported the data and added necessary annotations. Then the user is required to provide the preferred vtools association command to `COMMAND` variable. The vtools association command line parameters are the same as running this command on local desktop with an additional flag `-mpi` to indicate the job will be ran on the cluster. 

### 4. Submit job

After LSF script submitted with bsub, the job will be launched to run on the cluster with mpiexec, the communication between main node and worker nodes is handeld through zeroMQ. 
