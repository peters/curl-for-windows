# Curl for windows

Curl is a command line tool for transferring data specified with URL
syntax. Find out how to use curl by reading the curl.1 man page or the
MANUAL document. Find out how to install Curl by reading the INSTALL
document.

libcurl is the library curl is using to do its job. It is readily
available to be used by your software. 

# What?

Build a statically linked version of Curl on Windows.
Even sweeter, you can do it in like 10 minutes! 

# Motivation

Not having an up to date curl library on Windows ;)

# How?

Gyp! ;)

# Obtaining updates

  $ git fetch
  $ git submodule update --recursive

And rebuild as usual ;)
  
# Curl dependencies (git submodules in this repository)

- [Curl](https://github.com/bagder/curl): 7.30.0
- [Openssl](https://github.com/openssl/openssl): 1.0.0.1e
- [Libssh2](Libssh2.org): 2.1.4.3
- [Zlib](http://zlib.net): 1.2.5

# Prerequisites

* [Python 2.7](python.org)
* [Gyp](https://code.google.com/p/gyp/wiki/GypVsCMake)
* [Ninja](http://martine.github.io/ninja/) (optional, but it's awesome sauce! ;)

# Obtaining prerequisites 

NB! *Remember to install python first!*

    $ svn checkout http://gyp.googlecode.com/svn/trunk build\gyp
    $ git clone git://github.com/martine/ninja.git build\ninja
    $ cd ninja
    $ configure
    $ bootstrap
	
Add gyp and ninja to your windows path environment variable.

# Obtaining curl/dependencies
	
    $ git clone https://www.github.com/peters/curl-for-windows
    $ git submodule update --init --recursive
	
# Building with ninja

	  $ gyp --depth=. -f ninja curl.gyp
	  $ ninja -C out/Debug
	  $ ninja -C out/Release

*Takes about 30 seconds to build libcurl with ninja.*
	
# Building with Visual Studio

	  $ gyp --depth=. -f msvs curl.gyp
	
# Simple curl example
```
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
	- <mypath>/curl/include

- Add additional library search directory
	- <mypath>/out/<Debug|Release>/obj
	
- Link with the following libraries
  - libcurl.lib
  - openssl.lib
  - libssh2.lib
  - zlib.lib
  - wsock32.lib
  - wldap32.lib
  - ws2_32.lib
  
By now you should have sweet, statically linked, CURL! ;)
