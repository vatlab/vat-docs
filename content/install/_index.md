+++
title = "Installation"
weight = 1
+++


# Installing variant tools

variant tools / variant association tools is available on Mac OSX, and posix systems such as Linux, Unix and Solaris. It is distributed under a [GNU Public License (V3)][2], which means that you are free to use, change, and share this software. Due to the nature of next-gen sequencing data, a reasonably powerful machine is needed to use this tool for real-world applications. 



### Compile from source if you have a standard Python installation

If you have a standard Python installation (Python 2.7.1 or Python 3.3 or higher), you can install variant tools using command `pip` 



    % pip install variant_tools
    

If you already have variant tools installed and would like to update to the newest version, run 



    % pip install variant_tools --upgrade
    

to download and compile variant tools from source. 



### Direct installation for Anaconda Python 

If you are using anaconda python, you can install variant tools using command 



    % conda install -c https://conda.binstar.org/bpeng variant_tools
    

If you already have variant tools installed, running 



    % conda update -c https://conda.binstar.org/bpeng variant_tools
    

would update variant tools to the newest version. 



### Download and compile from source code (for advanced users)

If no binary distribution is available for your platform or if you would like to perform a site-wide installation (see next section), you can build *variant tools* from source. 



#### Prerequisites:

*   Python 



*variant tools* requires Python 2.7.1 or higher, or Python 3.2 or higher. Please make sure you have the right version of python before you install variant tools. 



 ![][3]

**Mac OSX** 



Mac OSX Lion (10.7) comes with Python 2.7.1, which is compatible with variant tools. You can also download and install Python 3 from the Python website. 



 ![][4]

**Linux** 



The latest version of Ubuntu has recent versions of Python 2 and Python 3. Redhat Linux comes with Python 2.6. You will have to upgrade it to Python 2.7, or install Python 3. Because header files are sometimes provided as separate packages, you will need to install packages such as `python-dev` or `python3-dev` (Ubuntu) if you see error messages related to missing header files. For example, Ubuntu and other debian-derived systems need to install packages `python-dev`, `swig` (if using development version), `build-essential`, and `libbz2-dev`. 



*   simuPOP (version 1.1.4 or higher) for the use of Variant Simulation Tools 



You will need to install a recent version (1.1.4 or higher) of [simuPOP][5] if you plan to use [*Variant Simulation Tools*][6][?][6] to simulate data (command `vtools simulate`). 



1.  A C/C++ compiler 



 ![][4]

**Linux (gcc)** 



Gcc is generally available for all Linux systems 



 ![][3]

**MaxOS X (gcc or clang)** 



For MacOSX Lion (10.7), please install the latest version of Xcode, and [Command Line Tools for Xcode][7] if you are using Xcode 4.3.2 or later. If you wish to create Installer packages with PackageMaker, you will also need to install PackageMaker, which is in the “Auxiliary Tools for Xcode” package as of Xcode 4.3. The download page for this package can be opened via the Xcode -> Open Developer Tool -> More Developer Tools... menu item. After downloading and mounting the disk image, drag the PackageMaker application to your /Applications directory. 



#### Installing variant tools

After downloading the variant tools package, please run 



    % tar -xvzf variant_tools-VERSION.tar.gz
    % cd variant_tools-VERSION
    % (optionally, adjust site-wide options in source/site_options.py, see next section)
    % sudo python setup.py install
    



or 



    sudo python3 setup.py install
    



if you would like to use Python 3. 



If you get error messages for missing header files, please check if you have `zlib` and `bzip2` library and header files installed. You might need to install packages such as `bzip2-devel` and `zlib-devel` under linux. 



Commands `vtools` and `vtools_report` in the source code directory will not work. Please move out of the installation directory and execute globally installed commands. 



### Installing variant tools locally

variant tools consists of commands `vtools` and `vtools_report`, which are usually installed to `/usr/local/bin`. If you would like to install variant tools to a local directory, please use commands such as 



    % python setup.py install --install-platlib=~/python_lib \
                            --install-scripts=~/bin
    

In this way, the variant tools library will be installed to `~/python_lib`, and the `vtools` and `vtools_report` commands will be installed to `~/bin`. You will need to add `~/bin` to `$PATH`, and set environment variables `PYTHONPATH` to refer to `~/python_lib` so that python can find the library. If you are using bash, you can set these paths by adding the following two lines at the end of your `.bashrc` file: 



    % export PATH=~/bin:$PATH
    % export PYTHONPATH=~/python_lib
    



### Building the development version of variant tools

If you would like to try the absolute newest version of variant tools, you can check out variant tools from its sourceforge git repository. Under linux, you can simply run 



    % git clone git://git.code.sf.net/p/varianttools/git varianttools
    % cd varianttools
    % python setup.py install  # or python3 setup.py install
    

If you have changed the C/C++ code, you will need to re-generate the Python wrapper using SWIG. If you are using the latest version of Ubuntu, you can get it from package `swig2.0`. The package `SWIG` under Redhat or CentOS at version 1.34 is also usable (but only for python 2). 



Due to a bug in type handling, some versions of swig (2.0.6 and 2.0.7 are confirmed) can not be used to build variant tools. Please use version 2.0.4 if you experience any swig related problem. 



### Troubleshooting

**1. Error message `ImportError: No module named variant_tools`.** 

If you used a customized local installation by setting `--install-platlib`, you will have to set `PYTHONPATH` to the specified directory (which should contain directory `variant_tools`). This can be done in the `.bashrc` file, or in a module file if a module management system is used. 

**2. Error message `Failed to import module (No module named _vt_sqlite3)`** 

We have noticed this problem under some special circumstances. The problem is caused by lacking read permission of `.so` files under `/path/to/site_package/variant_tools`. Using `chmod o+x /path/to/site_package/variant_tools/*.so` can fix the problem. 

**3. Use of clang compiler under MacOSX ** 

If you are using a version of Python downloaded from the Python official website, you might need to create a symbolic link of `gcc` as `gcc-4.2` using command 



    % ln -s /usr/bin/gcc /usr/bin/gcc-4.2
    

because these distributions are built using command "gcc-4.2". If you do not have gcc installed, clang could be used for variant tools version 1.0.3d or later. 

**4. MaxOS X MDK mismatch with non-system Python** 

The downloaded version of Python might not use the same version of Xcode and OS SDK that is available on your system. For example, the official package for Python 3.2.3 assumes a SDK path of `/Developer/SDKs/MacOSX10.6.sdk`, and will not work for Xcode 4.3.3 on OSX 10.7 with a SDK path of `/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.7.sdk`. To correct this problem, you will need to set `CFLAGS` explicitly, namely running 



    export CFLAGS=-sysroot,/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.7.sdk
    export LDFLAGS=-L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.7.sdk/usr/lib
    

before you call `python3 setup.py install` to compile variant tools. Also, in this particular configuration, the `vtools` and `vtools_report` executables will be put under `/Library/Frameworks/Python.framework/Versions/3.2/bin` instead of `/usr/local/bin`. You will either need to add `/Library/Frameworks/Python.framework/Versions/3.2/bin` to `$PATH`, or create symbolic links of those executables to `/usr/local/bin`. 



## Resource management for individual or site-wide installation

### Batch download of resources

The variant tools website hosts a large number of annotation databases and other resources. These files are downloaded automatically to a local resource directory (`~/.variant_tools`) when they are needed, and need not to be downloaded again. However, if you plan to use many of the variant tools resources and have enough disk space, you can download all variant tools resources into your local resource directory using commands 



    % vtools admin --update_resource
    

This command by default download all current resources (e.g. most recent versions of annotation databases for latest version of reference genome). You can however using option `hg18` to download resources for `hg18` 

    % vtools admin --update resource hg18
    

Multiple users could share the same local resource directory if you put these files under a directory that is writable by multiple users, and set runtime option `local_resource` to this directory using command "`vtools admin --set_runtime_option local_resource=XXX`". For example, you could download all resources to directory `/Data/vtools_resource` using commands 



    % vtools init temp
    % vtools admin --set_runtime_option local_resource=/Data/vtools_resource
    % vtools admin --update_resource all
    % vtools remove project
    

Note that the `all` option will download all versions of resources for all reference genomes and can take a lot of disk spaces (about 60G as of March 2013). 



You can set `shared_resource` during the variant tools installation so that you do not have to set `$local_resource` for each project. 



### Runtime options for site-wide installation from source code

If you are a system administrator, you can change the default values of runtime options such as `shared_resource`, `temp_dir`, and `search_path` before installing variant tools. These options are defined in `source/site_options.py`. You can change them before running `python setup.py install`, or modify them afterwards (under a directory named similar to `/usr/lib/python/lib/python2.7/site-packages/variant_tools`). 



1.  `temp_dir`. Users will by default use `/tmp` for temporary files. However, due to the size of next-gen sequencing data, `/tmp` might not have enough space for these files. You can set this option to a directory with more disk space if `/tmp` is small. 

2.  `shared_resource`. A directory for shared resource files. It can be configured as 
    *   No shared resource (default). All users maintain their own resource directory ($local\_resource, which is usually ~/.variant\_tools). 
    
    *   A read-only directory with a mirror of the variant tools repository, with .DB.gz files decompressed in the annoDB directory. This is important because otherwise each user will have to decompress the files in their local resource directory. The system admin can choose to remove outdated databases to reduce the use of disk space. This option requires regular update of the resources. 
    
    *   A directory that is writable by all users. The resources will be downloaded to this directory by users, and shared by all users. This option is easier to implement and requires less maintenance. A system administrator can choose to mirror the variant tools repository and let the users to keep it up to date. 
    

3.  `search_path`. This option is a ;-separated list of URL that host the variant tools repository. It should only be changed if you have created a local mirror of the variant tools repository. Adding the URL before the default URL might provide better downloading performance for your users. Removing the default URL is possible but not recommended. 



### Mirroring the variant tools repository 

You can mirror the variant tools repository and provide it either to local users or all users of variant tools. For example, you can run 



    % vtools admin --mirror_repository /path/to/mirror 
    

to create a local copy of the repository, and either 

1.  add `/path/to/mirror` or a URL to the mirror to `search_path` in `source/site_options.py`. Users will be able to download from this mirror with better performance, or 
2.  set `/path/to/mirror` as `shared_resource` so that users can use them directly. You can set this directory as read-only so that users cannot change the content of this directory. 

We always look for public mirrors for our repository. Your help would be highly appreciated if you could send us the URL so that we can make it a public mirror for all variant tools users. 



1.  The `vtools admin --mirror_repository` command should be run regularly to keep the mirror updated. It is recommended that you set it up as a daily cron job. 
2.  The variant tools repository is split into a main repository and an archive repository. You generally need only to mirror the main repository. The archive repository contains earlier versions of annotation databases that are kept for reproducibility reasons.

 []: http://sourceforge.net/projects/varianttools/files/
 [2]: http://www.gnu.org/copyleft/gpl.html
 [3]: http://simupop.sourceforge.net/images/osmac.gif ""
 [4]: http://simupop.sourceforge.net/images/oslinux.png ""
 [5]: http://simupop.sourceforge.net
 [6]: http://localhost/~iceli/wiki/pmwiki.php?n=Simulation.HomePage?action=edit
 [7]: https://developer.apple.com/downloads/index.action?=command%20line%20tools