from distutils.core import setup
from distutils.extension import Extension
import os
import sys
import platform


#openmm_dir = '/home/jtufts/anaconda3/envs/openmm'
#randombatchewaldplugin_header_dir = '/home/jtufts/src/p310/openmm_rbe/openmm_rbe/openmmapi/include'
#randombatchewaldplugin_library_dir = '/home/jtufts/src/p310/openmm_rbe/openmmrandombatchewald_build'

openmm_dir = '/home/jtufts/anaconda3/envs/openmm/include'
randombatchewaldplugin_header_dir = '/home/jtufts/src/p310/openmm_rbe/openmm_rbe/openmmapi/include'
randombatchewaldplugin_library_dir = '/home/jtufts/src/p310/openmm_rbe/openmm_rbe/openmmapi/src'

print(randombatchewaldplugin_header_dir, randombatchewaldplugin_library_dir)
# setup extra compile and link arguments on Mac
extra_compile_args = ['-std=c++11']
extra_link_args = []

if platform.system() == 'Darwin':
    extra_compile_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7']
    extra_link_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7', '-Wl', '-rpath', openmm_dir+'/lib']

extension = Extension(name='_randombatcheqaldplugin',
                      sources=['openmm_rbe/RandomBatchEwaldPluginWrapper.cpp'],
                      libraries=['OpenMM', 'OpenMMRandomBatchEwald'],
                      include_dirs=[os.path.join(openmm_dir, 'include'), randombatchewaldplugin_header_dir],
                      library_dirs=[os.path.join(openmm_dir, 'lib'), randombatchewaldplugin_library_dir],
                      extra_compile_args=extra_compile_args,
                      extra_link_args=extra_link_args
                     )

setup(name='randombatchewaldplugin',
      version='0.1',
      py_modules=['openmm_rbe/randombatchewaldplugin'],
      ext_modules=[extension],
)
