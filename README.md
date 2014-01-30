# Curl for windows

Curl is a command line tool for transferring data specified with URL
syntax. Find out how to use curl by reading the curl.1 man page or the
MANUAL document. Find out how to install Curl by reading the INSTALL
document.

libcurl is the library curl is using to do its job. It is readily
available to be used by your software. 

# About

This repository is a collection of submodules (dependencies)
that curl need to build successfully. Each submodule tracks
the latest known git release tag. In order to make 
this easy to maintain i converted the buildsystem to GYP. 
Please note that this is not a **_FORK_** and no patches has
been applied or sent upstream.

By following the tutorial below, you should be able build
a working, statically linked version of the latest libcurl.

**Both x86 and x64 builds are supported.**

Happy linking ;)

# Download prebuilt version of curl

Download available for your convenience over at [SourceForge](https://sourceforge.net/projects/curlforwindows/files/?source=navbar) which
also includes the static libraries.

# Obtaining a free copy of visual studio

If you do not have a visual studio license you can
download [Visual Studio 2013 Express edition](http://go.microsoft.com/?linkid=9816758) for free.

# Curl dependencies

- [Openssl](https://github.com/openssl/openssl): 1.0.0.1e
- [Libssh2](http://libssh2.org): 2.1.4.3
- [Zlib](http://zlib.net): 1.2.8

# Prerequisites

* [Python 2.7](python.org)

# Obtaining prerequisites 
	
    $ git clone https://github.com/peters/curl-for-windows.git
    $ git submodule update --init --recursive
      
# Configuration options
    
    $ python configure.py --help

```
Usage: configure.py [options]

Options:
  -h, --help            show this help message and exit
  --toolchain=TOOLCHAIN
                        msvs toolchain to build for. [default: auto]
  --target-arch=TARGET_ARCH
                        CPU architecture to build for. [default: x86]
```

# Generate project files

    $ python configure.py 

Open respective **curl.sln** found in **out** folder ;)

# Simple curl example

If you are new to curl you can checkout the example project
found in curl.sln or you can view additional the **[examples](https://github.com/bagder/curl/tree/master/docs/examples)**
in the official curl repository.

# Linking with libcurl (without gyp)

- Add preprocessor flag 
  - CURL_STATICLIB
 
- Add include directory
	- path/to/curl/include

- Add additional library search directory
	- path/to/out/Debug|Release/obj
	
- Link with the following libraries
  - libcurl.lib
  - openssl.lib
  - libssh2.lib
  - zlib.lib
  - wsock32.lib
  - wldap32.lib
  - ws2_32.lib
  
By now you should have sweet, statically linked, CURL! ;)
