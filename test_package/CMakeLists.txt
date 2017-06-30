project(PackageTest CXX)
cmake_minimum_required(VERSION 3.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

target_compile_options(example PRIVATE $<$<CXX_COMPILER_ID:MSVC>:/std:c++latest>)
set_target_properties(example PROPERTIES CXX_STANDARD 17 CXX_STANDARD_REQUIRED ON)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
