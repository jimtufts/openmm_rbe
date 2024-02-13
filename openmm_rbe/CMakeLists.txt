cmake_minimum_required(VERSION 3.28)
project(OpenMMRandomBatchEwald)
set(WRAP_FILE RandomBatchEwaldPluginWrapper.cpp)
set(MODULE_NAME randombatchewaldplugin)
SET(OPENMM_DIR "/home/jtufts/anaconda3/envs/openmm" CACHE PATH "Where OpenMM is installed")
# Execute SWIG to generate source code for the Python module.

add_custom_command(
    OUTPUT "${WRAP_FILE}"
    COMMAND "${SWIG_EXECUTABLE}"
        -python -c++
        -o "${WRAP_FILE}"
        "-I${OPENMM_DIR}/include"
        "${CMAKE_CURRENT_SOURCE_DIR}/randombatchewaldplugin.i"
    DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/randombatchewaldplugin.i"
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
)

# Compile the Python module.

add_custom_target(PythonInstall DEPENDS "${WRAP_FILE}")
set(RANDOMBATCHEWALDPLUGIN_HEADER_DIR "${CMAKE_SOURCE_DIR}/openmmapi/include")
set(RANDOMBATCHEWALDPLUGIN_LIBRARY_DIR "${CMAKE_BINARY_DIR}")
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../setup.py ${CMAKE_CURRENT_BINARY_DIR}/../setup.py)
add_custom_command(TARGET PythonInstall
    COMMAND "${PYTHON_EXECUTABLE}" ../setup.py build
    COMMAND "${PYTHON_EXECUTABLE}" ../setup.py install
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
)

