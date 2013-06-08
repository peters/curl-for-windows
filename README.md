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
the latest known release tag. (See below for specific version). In order to make 
this easy to maintain i converted the buildsystem to GYP. 
Please note that this is not a **_FORK_** and no patches has
been applied or sent upstream.

By following the tutorial below, you should be able build
a working, statically linked version of the latest libcurl.

**NB** The curl executable is not being built, but i
plan to provide that in the nearest future.

Happy linking ;)

# Obtaining updates

    $ git pull
    $ git submodule update --recursive
    
And rebuild as usual ;)
  
# Curl dependencies

- [Curl](https://github.com/bagder/curl): 7.30.0
- [Openssl](https://github.com/openssl/openssl): 1.0.0.1e
- [Libssh2](http://libssh2.org): 2.1.4.3
- [Zlib](http://zlib.net): 1.2.5

# Prerequisites

* [Python 2.7](python.org)
* [Gyp](https://code.google.com/p/gyp/wiki/GypVsCMake)

# Obtaining prerequisites 
	
    $ git clone https://www.github.com/peters/curl-for-windows
    $ git submodule update --init --recursive

# Generate project files

    $ python configure.py 
    $ python configure.py --target-arch=x64
    
Or a specific msvs toolchain:

    $ python configure.py --toolchain=[2008,2010,2012]
    
Open respective **curl.sln** found in **out** folder ;)

# Simple curl example

If you are new to curl you can checkout the example project
found in curl.sln or you can find additional examples [https://github.com/bagder/curl/tree/master/docs/examples](here).


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
