# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'includes': [
    'common.gypi',
  ],
  'variables' : {
	'os_bsd': 0
  },
  'targets': [
    {
      'target_name': 'zlib',
      'type': '<(library)',
      'sources': [
		# minizip
		'zlib/contrib/minizip/ioapi.c',
        'zlib/contrib/minizip/ioapi.h',
        'zlib/contrib/minizip/iowin32.c',
        'zlib/contrib/minizip/iowin32.h',
        'zlib/contrib/minizip/unzip.c',
        'zlib/contrib/minizip/unzip.h',
        'zlib/contrib/minizip/zip.c',
        'zlib/contrib/minizip/zip.h',
		# zlib
        'zlib/adler32.c',
        'zlib/compress.c',
        'zlib/crc32.c',
        'zlib/crc32.h',
        'zlib/deflate.c',
        'zlib/deflate.h',
        'zlib/gzclose.c',
        'zlib/gzguts.h',
        'zlib/gzlib.c',
        'zlib/gzread.c',
        'zlib/gzwrite.c',
        'zlib/infback.c',
        'zlib/inffast.c',
        'zlib/inffast.h',
        'zlib/inffixed.h',
        'zlib/inflate.c',
        'zlib/inflate.h',
        'zlib/inftrees.c',
        'zlib/inftrees.h',
        'build/mozzconf.h',
        'zlib/trees.c',
        'zlib/trees.h',
        'zlib/uncompr.c',
        'zlib/zconf.h',
        'zlib/zlib.h',
        'zlib/zutil.c',
        'zlib/zutil.h',
      ],
      'include_dirs': [
		'build', # mozzconf.h
		'zlib',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
		  'zlib',
		  # For contrib/minizip
		  './contrib/minizip',
        ],
      }
    },
  ],
}