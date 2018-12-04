+++
title = "association analysis on cluster"
weight = 7
hidden = true
+++


## Run association analysis on cluster

Since vtools association analysis is quite time consuming, meanwhile this job could be easily distributed to run on multiple nodes. Here we show an example to demonstrate how to run vtools association job on a PBS cluster.

The example PBS script is `vtools_association_cluster.pbs` in `/src/variant_tools` folder. 

### 1. Header of PBS script

Like any other PBS scripts, user first specifies the number of nodes and cores assigned to run this job. In this example, we will use four nodes and eight cores from each node. The job will be submitted to a job queue named short.

    #!/bin/bash
    #PBS -l nodes=4:lowmem:ppn=8,walltime=01:00:00
	#PBS -V
	#PBS -q short

### 2. Specify project folder

User needs to specify the folder path to the existing vtools project (The folder created by `vtools init` command) by assigning the folder path to `PROJECTFOLDER`. 

### 3. Specify the vtools association command

At this step, user should have already imported the data and added necessary annotations. Then the user is required to provide the preferred vtools association command to `COMMAND` variable. The vtools association command line parameters are the same as running this command on local desktop except an additional flag `-mpi` to indicate the job will be ran on the cluster. 

### 4. Submit job

After PBS script submitted with qsub, the job will be launched to run on the cluster with mpiexec, the communication between main node and worker nodes is handeld through zeroMQ. 


