# Copyright Joyent, Inc. and other Node contributors.
# 2013 (C) Peter Rekdal Sunde
{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'zlib',
      'type': '<(library)',
      'include_dirs': [
        'zlib',
        'zlib/contrib/minizip',
      ],
      'sources': [
        'zlib/contrib/minizip/ioapi.c',
        'zlib/contrib/minizip/ioapi.h',
        'zlib/contrib/minizip/iowin32.c',
        'zlib/contrib/minizip/iowin32.h',
        'zlib/contrib/minizip/unzip.c',
        'zlib/contrib/minizip/unzip.h',
        'zlib/contrib/minizip/zip.c',
        'zlib/contrib/minizip/zip.h',
        'zlib/adler32.c',
        'zlib/compress.c',
        'zlib/crc32.c',
        'zlib/crc32.h',
        'zlib/deflate.c',
        'zlib/deflate.h',
        'zlib/gzio.c',
        'zlib/infback.c',
        'zlib/inffast.c',
        'zlib/inffast.h',
        'zlib/inffixed.h',
        'zlib/inflate.c',
        'zlib/inflate.h',
        'zlib/inftrees.c',
        'zlib/inftrees.h',
        'zlib/mozzconf.h',
        'zlib/trees.c',
        'zlib/trees.h',
        'zlib/uncompr.c',
        'zlib/zconf.h',
        'zlib/zlib.h',
        'zlib/zutil.c',
        'zlib/zutil.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'zlib'
        ]
      },
      'conditions': [
        ['OS!="win"', {
            'product_name': 'chrome_zlib',
            'cflags!': ['-ansi'],
            'sources!': [
            'contrib/minizip/iowin32.c'
          ],
        }],
      ],
    },
  ],
}