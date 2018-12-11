+++
title = "association analysis on cluster using PBS"
weight = 7
hidden = true
+++


## Run association analysis on cluster using PBS

Since vtools association analysis is quite time consuming, meanwhile this job could be easily distributed to run on multiple nodes. Here we show an example to demonstrate how to run vtools association job on cluster using PBS.

The example PBS script is `vtools_association_cluster.pbs` in `/src/variant_tools` folder. 
Please make sure the `openmpi` module is loaded, so that `mpiexec` command could be executed.

### 1. Header of PBS script

Like any other PBS scripts, user first specifies the number of nodes and cores assigned to run this job. In this example, we will use four nodes and eight cores from each node. The job will be submitted to a job queue named short.

    #!/bin/bash
    #PBS -l nodes=4:lowmem:ppn=8,walltime=01:00:00
	#PBS -V
	#PBS -q short

### 2. Specify project folder

User needs to specify the folder path to the existing vtools project (The folder created by `vtools init` command) by assigning the folder path to `PROJECTFOLDER`. PROJECTFOLDER could be set as an environmental variable or given a value in the script.

### 3. Specify the vtools association command

At this step, user should have already imported the data and added necessary annotations. Then the user is required to provide the preferred vtools association command to `COMMAND` variable. The vtools association command line parameters are the same as running this command on local desktop with an additional flag `-mpi` to indicate the job will be ran on the cluster. 

### 4. Specify the number of processes per node

If user claim to use four nodes, one of the nodes will be used to run main program, the other three nodes will be taken as worker nodes. If user use eight cores per node, then `NUMBER_OF_PROCESSES_PER_NODE` could be set to 8. 


### 5. Submit job

After PBS script submitted with qsub, the job will be launched to run on the cluster with mpiexec, the communication between main node and worker nodes is handeld through zeroMQ. The result could be viewd in output file or saved into database with `--to_db` parameter set in association command. 


