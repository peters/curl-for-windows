# 2013 (C) Peter Rekdal Sunde

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
        'build', # curl configuration
        'curl',
        'curl/lib',
        'curl/include',
      ],
      'defines': [
        'USE_SSLEAY',
        'USE_IPV6',
        'USE_LIBSSH2',
        'USE_ZLIB',
        'USE_WINDOWS_SSPI',
        'HAVE_SPNEGO',
        'HAVE_ZLIB_H',
        'HAVE_LIBSSH2_H',
        'HAVE_ZLIB',
        'HAVE_LIBZ',
        'BUILDING_LIBCURL',
      ],
      'dependencies': [
        'openssl.gyp:openssl',
        'zlib.gyp:zlib',
        'libssh2.gyp:libssh2'
      ],
      'direct_dependent_settings': {
        'conditions': [
          ['_type=="static_library"',
            {
              'defines':[
                'CURL_STATICLIB'
              ]
            }
          ]
        ],
        'include_dirs': [
          'curl/include',
          'build'
        ],
      },
      'sources':[
        'build/tool_hugehelp.c',
		'curl/lib/vtls/axtls.c',
		'curl/lib/vtls/curl_darwinssl.c',
		'curl/lib/vtls/curl_schannel.c',
		'curl/lib/vtls/cyassl.c',
		'curl/lib/vtls/gskit.c',
		'curl/lib/vtls/gtls.c',
		'curl/lib/vtls/nss.c',
		'curl/lib/vtls/openssl.c',
		'curl/lib/vtls/polarssl.c',
		'curl/lib/vtls/polarssl_threadlock.c',
		'curl/lib/vtls/qssl.c',
		'curl/lib/vtls/vtls.c',
        'curl/lib/dotdot.c',
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
        'curl/lib/tftp.c',
        'curl/lib/splay.c',
        'curl/lib/strdup.c',
        'curl/lib/socks.c',
        'curl/lib/ssh.c',
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
        'curl/lib/curl_rtmp.c',
        'curl/lib/openldap.c',
        'curl/lib/curl_gethostname.c',
        'curl/lib/gopher.c',
        'curl/lib/idn_win32.c',
        'curl/lib/http_negotiate_sspi.c',
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
        'curl/lib/curl_multibyte.c',
        'curl/lib/hostcheck.c',
        'curl/lib/bundles.c',
        'curl/lib/conncache.c',
        'curl/lib/pipeline.c',
      ],
      'conditions':[
        ['OS=="win"',
          {
            'link_settings': {
              'libraries': [
                '-lws2_32.lib',
                '-lwldap32.lib',
                '-ladvapi32.lib',
              ],
            },
          }
        ],
        ['OS!="mac"',
          {
          # todo
          },
          {
          # linux
          }
        ],
        ['_type=="static_library"',
          {
            'defines':[
              'CURL_STATICLIB'
            ]
          }
        ]
      ],
    },
	{
	  'target_name': 'curl',
	  'type': 'executable',
	  'dependencies': [
		'libcurl',
	  ],
	  'include_dirs': [
        '.',
        'curl/lib',		
        'curl/src',
	  ],
	  'defines': [
       
	  ],
	  'sources': [
      'curl/src/tool_binmode.c',
      'curl/src/tool_bname.c',
      'curl/src/tool_cb_dbg.c',
      'curl/src/tool_cb_hdr.c',
      'curl/src/tool_cb_prg.c',
      'curl/src/tool_cb_rea.c',
      'curl/src/tool_cb_see.c',
      'curl/src/tool_cb_wrt.c',
      'curl/src/tool_cfgable.c',
      'curl/src/tool_convert.c',
      'curl/src/tool_dirhie.c',
      'curl/src/tool_doswin.c',
      'curl/src/tool_easysrc.c',
      'curl/src/tool_formparse.c',
      'curl/src/tool_getparam.c',
      'curl/src/tool_getpass.c',
      'curl/src/tool_help.c',
      'curl/src/tool_helpers.c',
      'curl/src/tool_homedir.c',
      'curl/src/tool_libinfo.c',
      'curl/src/tool_main.c',
      'curl/src/tool_metalink.c',
      'curl/src/tool_mfiles.c',
      'curl/src/tool_msgs.c',
      'curl/src/tool_operate.c',
      'curl/src/tool_operhlp.c',
      'curl/src/tool_panykey.c',
      'curl/src/tool_paramhlp.c',
      'curl/src/tool_parsecfg.c',
      'curl/src/tool_setopt.c',
      'curl/src/tool_sleep.c',
      'curl/src/tool_urlglob.c',
      'curl/src/tool_util.c',
      'curl/src/tool_vms.c',
      'curl/src/tool_writeenv.c',
      'curl/src/tool_writeout.c',
      'curl/src/tool_xattr.c',
	  ],
	},
    {
      'target_name': 'example',
      'type': 'executable',
      'dependencies': [
        'libcurl',
      ],
      'sources' : [
        'example.c'
      ],	  
    },
    #{
      # todo: tests
    #}
  ],
}
