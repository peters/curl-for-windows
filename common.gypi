# Copyright Joyent, Inc. and other Node contributors.
# 2013 (C) Peter Rekdal Sunde

{
  'variables': {
    'target_arch%': 'x86',
    'library%': 'static_library',
    'openssl_enable_asm%': 0, # todo: fix support for asm generation on windows
    'gcc_version%': 0,
    'is_clang%': 0,
  },
  'target_defaults': {
    'default_configuration': 'Release',
    'defines': [
      'USE_SSLEAY',
      'USE_IPV6',
      'USE_SSH2',
      'USE_ZLIB',
      'USE_WINDOWS_SSPI',
      'HAVE_SPNEGO',
      'HAVE_ZLIB_H',
      'HAVE_ZLIB',
      'HAVE_LIBZ',
      'USE_IDN=false',
      'USE_WINSSL=false',
      'Machine=<(target_arch)',
    ],
    'configurations': {
      'Debug': {
        'defines': [
          'DEBUG',
          '_DEBUG'
        ],
        'cflags': [
          '-g',
          '-O0'
        ],
        'conditions': [
          ['target_arch=="x64"', {#
              'msvs_configuration_platform': 'x64',
            }
          ],
        ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1,
            #static debug 'Optimization': 0,
            #/Od, no optimization
            'MinimalRebuild': 'false',
            'OmitFramePointers': 'false',
            'BasicRuntimeChecks': 3, # /RTC1
          },
          'VCLinkerTool': {
            'LinkIncremental': 2,
            #enable incremental linking
          },
        },
      },
      'Release': {
        'msvs_settings': {

          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, #static release 
            'Optimization': 3, #/Ox, full optimization
						'FavorSizeOrSpeed': 1, # /Ot, favour speed over size 
						'InlineFunctionExpansion': 2, #/Ob2, inline anything eligible
						'WholeProgramOptimization': 'true', # /GL, whole program optimization, needed for LTCG 
						'OmitFramePointers': 'true',
            'EnableFunctionLevelLinking': 'true',
            'EnableIntrinsicFunctions': 'true',
            'RuntimeTypeInfo': 'false',
            'ExceptionHandling': '0',
            'AdditionalOptions': [
              '/MP', #compile across multiple CPUs
            ],
          },
          'VCLibrarianTool': {
            'AdditionalOptions': [
              '/LTCG', #link time code generation
            ],
          },
          'VCLinkerTool': {
            'LinkTimeCodeGeneration': 1, #link - time code generation 
            'OptimizeReferences': 2, #/OPT:REF
						'EnableCOMDATFolding': 2, # /OPT: ICF 'LinkIncremental': 1,
            #disable incremental linking
          },
        },
      },
      'msvs_settings': {
        'VCCLCompilerTool': {
          'StringPooling': 'true', #pool string literals 
          'DebugInformationFormat': 3, #Generate a PDB 
          'WarningLevel': 3,
          'BufferSecurityCheck': 'true',
          'ExceptionHandling': 1, #/EHsc
	        'SuppressStartupBanner': 'true',
	        'WarnAsError': 'false',
      	},
      	'VCLinkerTool': 
      	{
	        'conditions': 
	        [
	          ['target_arch=="x64"', {
	            'TargetMachine': 17 # /MACHINE:X64
	          }],
	        ],
	        'GenerateDebugInformation': 'true',
	        'RandomizedBaseAddress': 2, # enable ASLR
	        'DataExecutionPrevention': 2, # enable DEP
	        'AllowIsolation': 'true',
	        'SuppressStartupBanner': 'true',
	        'target_conditions': [
	          ['_type=="executable"', {
	            'SubSystem': 1, # console executable
	          }],
	         ],
      	},
      },
    },
  },
}