# 2013 (C) Peter Rekdal Sunde

# features:
# -> libcurl/curl is statically linked with latest openssl/libssh2/zlib libraries
# -> tested building both in debug/release on VC10, VC11

# todo: 
# -> fix asm build on windows for openssl
# -> fix building shared libraries
# -> write a configure script in python (enable/disable features)
# ---> https://github.com/joyent/node/blob/master/configure)

{
  'includes': [
    'common.gypi',
  ],
  'targets': 
  [
    {
      'target_name': 'libcurl',
      'type': '<(library)',
      'include_dirs': [
     		'.',
     		'curl',
     		'curl/lib',
     		'curl/include',
  		],
      'defines': [
     		'BUILDING_LIBCURL',
  		],
      'dependencies': [
     		'openssl.gyp:openssl',
     		'zlib.gyp:zlib',
     		'libssh2.gyp:libssh2'
  		],
      'direct_dependent_settings': [
     		'curl/include'
  		],
      'sources':[
        'curl/src/tool_hugehelp.h',
        'curl/lib/file.c',
        'curl/lib/timeval.c',
        'curl/lib/base64.c',
        'curl/lib/hostip.c',
        'curl/lib/progress.c',
        'curl/lib/formdata.c',
        'curl/lib/cookie.c',
        'curl/lib/http.c',
        'curl/lib/sendf.c',
        'curl/lib/ftp.c',
        'curl/lib/url.c',
        'curl/lib/dict.c',
        'curl/lib/if2ip.c',
        'curl/lib/speedcheck.c',
        'curl/lib/ldap.c',
        'curl/lib/ssluse.c',
        'curl/lib/version.c',
        'curl/lib/getenv.c',
        'curl/lib/escape.c',
        'curl/lib/mprintf.c', 
        'curl/lib/telnet.c',
        'curl/lib/netrc.c',
        'curl/lib/getinfo.c',
        'curl/lib/transfer.c',
        'curl/lib/strequal.c',
        'curl/lib/easy.c',
        'curl/lib/security.c',
        'curl/lib/krb4.c',
        'curl/lib/curl_fnmatch.c',
        'curl/lib/fileinfo.c',
        'curl/lib/ftplistparser.c',
        'curl/lib/wildcard.c',
        'curl/lib/memdebug.c',
        'curl/lib/http_chunks.c',
        'curl/lib/strtok.c',
        'curl/lib/connect.c',
        'curl/lib/llist.c',
        'curl/lib/hash.c',
        'curl/lib/multi.c', 
        'curl/lib/content_encoding.c',
        'curl/lib/share.c',
        'curl/lib/http_digest.c',
        'curl/lib/md4.c',
        'curl/lib/md5.c',
        'curl/lib/curl_rand.c',
        'curl/lib/http_negotiate.c',
        'curl/lib/inet_pton.c',
        'curl/lib/strtoofft.c',
        'curl/lib/strerror.c',
        'curl/lib/amigaos.c',
        'curl/lib/hostasyn.c',
        'curl/lib/hostip4.c',
        'curl/lib/hostip6.c', 
        'curl/lib/hostsyn.c',
        'curl/lib/inet_ntop.c',
        'curl/lib/parsedate.c',
        'curl/lib/select.c',
        'curl/lib/gtls.c',
        'curl/lib/sslgen.c',
        'curl/lib/tftp.c',
        'curl/lib/splay.c',
        'curl/lib/strdup.c',
        'curl/lib/socks.c',
        'curl/lib/ssh.c',
        'curl/lib/nss.c',
        'curl/lib/qssl.c',
        'curl/lib/rawstr.c',
        'curl/lib/curl_addrinfo.c',
        'curl/lib/socks_gssapi.c',
        'curl/lib/socks_sspi.c',
        'curl/lib/curl_sspi.c',
        'curl/lib/slist.c',
        'curl/lib/nonblock.c',
        'curl/lib/curl_memrchr.c',
        'curl/lib/imap.c',
        'curl/lib/pop3.c',
        'curl/lib/smtp.c',
        'curl/lib/pingpong.c',
        'curl/lib/rtsp.c',
        'curl/lib/curl_threads.c',
        'curl/lib/warnless.c',
        'curl/lib/hmac.c',
        'curl/lib/polarssl.c',
        'curl/lib/polarssl_threadlock.c',
        'curl/lib/curl_rtmp.c',
        'curl/lib/openldap.c',
        'curl/lib/curl_gethostname.c',
        'curl/lib/gopher.c',
        'curl/lib/axtls.c',
        'curl/lib/idn_win32.c',
        'curl/lib/http_negotiate_sspi.c',
        'curl/lib/cyassl.c',
        'curl/lib/http_proxy.c',
        'curl/lib/non-ascii.c',
        'curl/lib/asyn-ares.c',
        'curl/lib/asyn-thread.c',
        'curl/lib/curl_gssapi.c',
        'curl/lib/curl_ntlm.c',
        'curl/lib/curl_ntlm_wb.c', 
        'curl/lib/curl_ntlm_core.c',
        'curl/lib/curl_ntlm_msgs.c',    
        'curl/lib/curl_sasl.c',
        'curl/lib/curl_schannel.c', 
        'curl/lib/curl_multibyte.c',
        'curl/lib/curl_darwinssl.c',
        'curl/lib/hostcheck.c',
        'curl/lib/bundles.c',
        'curl/lib/conncache.c',
        'curl/lib/pipeline.c',
      ],
      'conditions':[
        ['OS=="win"', {
          'link_settings': {
            'libraries': [
              '-lws2_32.lib',
              '-lwldap32.lib',
              '-ladvapi32.lib',
            ],
          },        
        }],
        ['OS!="mac"', {
          # todo
        },{
          # linux
        }],
      ],
      'conditions': [
        ['_type=="static_library"', {
          'defines':[
            'CURL_STATICLIB'
          ]
        }]
      ],
    },
    
    #{
      # todo: examples
    #},
    #{
      # todo: tests
    #}
 ],
}