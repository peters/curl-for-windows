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
the latest known release tag. (See below for specific version).

In order to make this easy to maintain i converted the buildsystem
to GYP. Please note that this is not a **_FORK_** and no patches has
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
* [Ninja](http://martine.github.io/ninja/) (optional, but it's awesome sauce! ;)

# Obtaining prerequisites 
	
    $ git clone https://www.github.com/peters/curl-for-windows
    $ git submodule update --init --recursive

**Please note that all builds generates a valid PDB associated with either debug or release**

# Building with ninja (fastest)

    $ cd build\ninja
    $ python configure.py
    $ python bootstrap.py
    $ cd ..\..\
    $ python configure.py
    
You will find a release of libcurl in out\Release\obj.

# Building with Visual Studio

    $ python configure.py --msvs
		
Or a specific msvs toolchain:

    $ python configure.py --msvs --msvs-toolchain=[2008,2010,2012]
    
Open **curl.sln** ;)

# Building a debug version of libcurl
    
    $ python configure.py --debug

# Simple curl example
```c
#include <stdio.h>
#include <curl/curl.h>

int main(void)
{
  CURL *curl;
  CURLcode res;

  curl = curl_easy_init();
  if(curl) {
    curl_easy_setopt(curl, CURLOPT_URL, "http://example.com");
    /* example.com is redirected, so we tell libcurl to follow redirection */
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

    /* Perform the request, res will get the return code */
    res = curl_easy_perform(curl);
    /* Check for errors */
    if(res != CURLE_OK)
      fprintf(stderr, "curl_easy_perform() failed: %s\n",
              curl_easy_strerror(res));

    /* always cleanup */
    curl_easy_cleanup(curl);
  }
  if(::IsDebuggerPresent())
  {
    ::WaitForSingleObject(GetCurrentProcess(), INFINITE);
  }
  return 0;
}
```

# Additional examples

[https://github.com/bagder/curl/tree/master/docs/examples](Click here.)

# Linking with libcurl

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
